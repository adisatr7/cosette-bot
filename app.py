# Import necessary libraries
import nextcord
import modules.response_variety as respond
import wavelink
import re
from random import randint
from nextcord.ext import commands
from typing import List, Literal
from constants.prefixes import COMMAND_PREFIXES


# Declare Cosette's permissions
intents = nextcord.Intents.default()
intents.message_content = True
intents.presences = True

# Initializes Cosette
bot: commands.Bot = commands.Bot(
    command_prefix=COMMAND_PREFIXES,
    intents=intents
)

# Setting up wavelink node for Cosette's music player function
async def on_node():
    node: wavelink.Node = wavelink.Node(
        uri="http://narco.buses.rocks:2269",
        password="glasshost1984"
    )
    await wavelink.NodePool.connect(client=bot, nodes=[node])
    wavelink.Player.autoplay = True


# When Cosette is just started up
@bot.event
async def on_ready() -> None:

    # Declare Cosette's activity status
    activity = nextcord.Activity(
        name="to you",
        type=nextcord.ActivityType.listening
    )

    # Actually change the activity status
    await bot.change_presence(activity=activity)

    # Have Cosette send a greeting to the console
    print(f"{ respond.come_online() } \n")

    # Have Cosette connects to a node for her music player to function correctly
    bot.loop.create_task(on_node())


# When the Cosette receives a message in any channels she's in
@bot.event
async def on_message(message: nextcord.Message or None) -> None:

    # If Cosette is mentioned without further context, have her respond randomly
    if bot.user.mentioned_in(message):

        # Console log user's message
        print(f"{message.author}: \"{message.content}\"")

        # Have her respond to the chat
        response: str = response.respond_to_mention()
        await message.channel.send(response)


# Play command | TODO: Add Spotify support and USE EMBED
@bot.slash_command(guild_ids=[], description="Summon Cosette and let her work her magic with a YouTube jam")
async def play(
    interaction: nextcord.Interaction,
    search: str = nextcord.SlashOption(description="Enter the search query or YouTube URL of the song you want to play"),
    override: bool | None = nextcord.SlashOption(description="Override the current queue and start playing immediately (optional)")
) -> None:

    # Do a YouTube search
    query = await wavelink.YouTubeTrack.search(search, return_first=True)

    # Set the target voice channel where the user is in
    destination = interaction.user.voice.channel

    # If Cosette is not already in the voice channel, have her join one now
    if not interaction.guild.voice_client:
        vc: wavelink.Player = await destination.connect(cls=wavelink.Player)

    # Otherwise, stay there
    else:
        vc: wavelink.Player = interaction.guild.voice_client

    # If the queue is empty and the player is not playing, have Cosette play the song now
    if override or not vc.is_playing():
        await vc.play(query)
        await interaction.response.send_message(respond.starts_playing_a_song())

        # TODO: Replace with embed
        await interaction.channel.send(f"🎵  Now playing: **__{vc.current.title}__**")

    # Otherwise, add the song to queue
    elif not override:
        await vc.queue.put_wait(query)
        await interaction.response.send_message(respond.add_song_to_queue())

        # TODO: Replace with embed
        await interaction.channel.send(f"🎶  **__{query.title}__** has been added to queue!")


# Skip command
@bot.slash_command(guild_ids=[], description="Have Cosette to cue up the next melody in line.")
async def skip(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    try:
        if not vc.queue.is_empty:

            # Have Cosette tells the user that the song is skipped
            await interaction.response.send_message(respond.skip_song())

            # TODO: Use embed to display the next song info
            await interaction.channel.send(f"🎵  Now playing **__{vc.queue[0].title}__**")

            # Have Cosette stops the current song. The whole thing is set so that
            # it automatically plays the next song if the current one is stopped
            await vc.stop()

        else:
            await interaction.response.send_message(respond.no_more_songs())

    except nextcord.errors.ApplicationInvokeError as e:
        await interaction.response.send_message(respond.no_more_songs())


# Pause command
@bot.slash_command(guild_ids=[], description="Give Cosette a breather - even music bots need a quick break.")
async def pause(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    try:
        # If Cosette is currently playing a song, have her pause it now
        if not vc.is_paused():
            await vc.pause()

            # Have her tell the user that the song is paused
            await interaction.response.send_message(respond.pause())

        # Otherwise, have her tell the user that she's not playing anything
        else:
            await interaction.response.send_message(respond.song_already_paused())

    # Exception handler: When the bot is not in a voice channel
    except Exception as e:
        await interaction.response.send_message(respond.no_song())


# Resume command
@bot.slash_command(guild_ids=[], description="Get the music flowing again! Cosette's tunes can't stay quiet for long.")
async def resume(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    try:
        # If the current song is indeed being paused
        if vc.is_paused():

            # Have Cosette resumes it
            await vc.resume()

            # Have her tell the user that the song is already playing
            await interaction.response.send_message(respond.resume_song())

        # Otherwise, have her tell the user that the song is already resumed
        else:
            await interaction.response.send_message(respond.song_already_resumed())

    # Exception handler: When the bot is not in a voice channel
    except Exception as e:
        await interaction.response.send_message(respond.no_song())


# Stop command
@bot.slash_command(guild_ids=[], description="Hush Cosette's melodious purrs, leaving her song unfinished.")
async def stop(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # Have Cosette disconnects from the voice channel
    await vc.disconnect()

    # Have Cosette clears the music player queue
    if not vc.queue.is_empty:
        await vc.queue.clear()

    # Have Cosette tells the user a message as she leaves the voice channel
    await interaction.response.send_message(respond.leave_voice_channel())


# See queue command
@bot.slash_command(guild_ids=[], description="Peek into Cosette's song queue.")
async def queue(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    try:
        # If the queue is not empty
        if not vc.queue.is_empty:

            # Counts how many songs are in the queue
            song_counter: int = 0

            # Initializes the list of songs currently being queued by the music player
            songs: List[wavelink.PLayable | wavelink.SpotifyTrack] = []
            queue = vc.queue.copy()

            # Setup an embed message | TODO: Make it look better
            embed: nextcord.Embed = nextcord.Embed(title="Queue")

            for song in queue:
                song_counter += 1
                songs.append(song)
                embed.add_field(
                    name=f"[{song_counter}] Duration: {song.duration}",
                    value=song.title,
                    inline=False
                )

            # Send the embed message containing queue data to the user
            await interaction.response.send_message(embed=embed)

        # If the queue is empty
        else:

            # Have Cosette tells the user that the queue is indeed empty
            await interaction.response.send_message(respond.queue_is_empty())

    # Exception handler: If the 'queue' object is not initialized
    except AttributeError as e:

        # Have Cosette tells the user that she's not playing anything at the moment
        await interaction.response.send_message(respond.queue_is_empty())


# Roll dice command | TODO: Add response variety
@bot.slash_command(guild_ids=[], description="Have Cosette roll various dice for you TTRPG nerds.")
async def roll(
    interaction: nextcord.Interaction,
    die_type: Literal['d20', 'd12', 'd10', 'd100', 'd8', 'd6', 'd4', 'd2'] = nextcord.SlashOption(description="Choose the die type."),
    amount: int | None = nextcord.SlashOption(min_value=1, description="Set how many dice you want to roll. Defaults to 1 if left empty.")
) -> None:

    # Sets the max roll based on the die type used
    max_roll: int = int(re.findall(r"\d+", die_type)[0])

    # Prepares a variable named 'result' that can be an Integer or String
    rolled: int | str = 0

    # Prepares a variable named 'output' for the output, duh~
    output: str = ""

    # If user asks for multiple dice to be rolled
    if amount is not None and amount > 1:

        # Prepares a list of numbers to store all the results
        results: List[int] = []

        # Prepares an integer to store the total value of all rolls
        total: int = 0

        # Do the rolling
        for i in range(amount):
            rolled = randint(1, max_roll)
            total += rolled

            # Bold the result if it's a nat 1 or nat max
            if rolled == max_roll or rolled == 1:
                rolled = f"**{rolled}**"

            # Append the roll result into the list of results
            results.append(rolled)

        output = f"{results} \n**Total:** {total}"

    # If user asks for a single roll
    else:
        rolled = randint(1, max_roll)

        # Bold the result if it's a nat 1 or nat max
        output = f"**({rolled})**" if rolled == max_roll else f"({rolled})"

    # Send the roll result to the user
    await interaction.response.send_message(respond.rolling_dice())
    await interaction.channel.send(f"🎲 {amount or 1}{die_type} = { output }")


# Keep Cosette up and running by looping this whole process
bot.run("MTExNDIyMTM3NDc4NTk4MjUxNA.GlMPuw.dZyNhpd3e5QVeJSP0KDz80lQSmUzByORdAzBQ4")

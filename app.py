# Import necessary libraries
import nextcord
import modules.chat as chat
import wavelink
from nextcord.ext import commands
from typing import List
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
    print(f"{ chat.come_online() } \n")

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
        response: str = chat.respond_to_mention()
        await message.channel.send(response)


# Play command | TODO: Add Spotify support
@bot.slash_command(guild_ids=[], description="Summon Cosette and let her work her magic with a YouTube jam!")
async def play(interaction: nextcord.Interaction, search: str) -> None:

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
    if vc.queue.is_empty and not vc.is_playing():
        await vc.play(query)
        await interaction.response.send_message(f"Now playing: {vc.current.title}")

    # Otherwise, add the song to queue
    else:
        await vc.queue.put_wait(query)
        await interaction.response.send_message(f"{query.title} has been added to queue!")


# Skip command
@bot.slash_command(guild_ids=[], description="Have Cosette to cue up the next melody in line.")
async def skip(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # Have Cosette stops the current song. The whole thing is set so that
    # it automatically plays the next song if the current one is stopped
    await vc.stop()

    # Have Cosette tells the user that the song is skipped | TODO: Add response variety!
    await interaction.response.send_message("Song was skipped!")


# Pause command
@bot.slash_command(guild_ids=[], description="Give Cosette a breather - even music bots need a quick break.")
async def pause(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # If Cosette is currently playing a song, have her pause it now
    if not vc.is_paused():
        await vc.pause()

        # Have her tell the user that the song is paused
        await interaction.response.send_message("Song is paused!")

    # Otherwise, have her tell the user that she's not playing anything
    else:
        # TODO: Add response variety!
        await interaction.response.send_message("Song is already paused!")


# Resume command
@bot.slash_command(guild_ids=[], description="Get the music flowing again! Cosette's tunes can't stay quiet for long.")
async def resume(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # If the current song is indeed being paused
    if vc.is_paused():

        # Have Cosette resumes it
        await vc.resume()

        # Have her tell the user that the song is already playing
        await interaction.response.send_message("Song is resuming!")

    # Otherwise, have her tell the user that the song is already resumed
    else:
        await interaction.response.send_message("Song is already resumed!")


# Stop command
@bot.slash_command(guild_ids=[], description="Hush Cosette's melodious purrs, leaving her song unfinished.")
async def stop(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # Have Cosette disconnects from the voice channel
    await vc.disconnect()

    # Have Cosette clears the music player queue
    await vc.queue.clear()

    # Have Cosette tells the user that the music player has been stopped
    # TODO: Add response variety!
    await interaction.response.send_message("Song is stopped!")


# See queue command
@bot.slash_command(guild_ids=[], description="Peek into Cosette's song queue.")
async def queue(interaction: nextcord.Interaction) -> None:

    # Initializes Wavelink Player
    vc: wavelink.Player = interaction.guild.voice_client

    # If the queue is not empty
    if not vc.queue.is_empty:

        # Counts how many songs are in the queue
        song_counter: int = 0

        # Initializes the list of songs currently being queued by the music player
        songs: List[wavelink.PLayable | wavelink.SpotifyTrack] = []
        queue = vc.queue.copy()

        # Setup an embed message
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
        # TODO: Add response variety!
        await interaction.response.send_message("The queue is empty!")


# Keep Cosette up and running by looping this whole process
bot.run("MTExNDIyMTM3NDc4NTk4MjUxNA.GlMPuw.dZyNhpd3e5QVeJSP0KDz80lQSmUzByORdAzBQ4")

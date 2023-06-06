from nextcord import ButtonStyle, Color, Embed, Interaction, Message, SlashOption
from nextcord.errors import ApplicationInvokeError
from nextcord.ui import View, Button
from nextcord.ext import commands
import nextcord
import wavelink
import modules.response_variety as respond
import api.controllers as api


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        print("Music cog loaded successfully!")

    # Play command | TODO: Add Spotify support
    @nextcord.slash_command(guild_ids=[], description="Summon Cosette and let her work her magic with a YouTube jam")
    async def play(
        self,
        interaction: Interaction,
        search: str = SlashOption(
            description="Enter the search query or YouTube URL of the song you want to play"),
        override: bool | None = SlashOption(
            description="Play the new song immediately, replacing the one curently playing (optional)")
    ) -> None:

        # Remembers which text channel the command is executed from
        api.set_command_channel(interaction.guild_id, interaction.channel_id)

        # Do a YouTube search
        query = await wavelink.YouTubeTrack.search(search, return_first=True)

        # Set the target voice channel where the user is in
        try:
            destination = interaction.user.voice.channel

        # Exception handler: If the user is not in a voice channel
        # TODO: Test what happens if the user is in a voice channel that she has no permission to join
        except AttributeError as e:

            # Have Cosette respond to them via chat
            await interaction.response.send_message(respond.user_not_in_voice_channel())

            # End the function early
            return

        # If Cosette is not already in the voice channel, have her join one now
        if not interaction.guild.voice_client:
            vc: wavelink.Player = await destination.connect(cls=wavelink.Player)

        # If the user is in another channel, have Cosette move there
        elif interaction.guild.voice_client.channel != destination:
            vc: wavelink.Player = await interaction.guild.voice_client.move_to(destination)
            await interaction.response.send_message(respond.move_to_different_vc())

        # Otherwise, stay there
        else:
            vc: wavelink.Player = interaction.guild.voice_client

        # If the queue is empty and the player is not playing, have Cosette play the song now
        if override or not vc.is_playing():
            await vc.play(query)
            await interaction.response.send_message(respond.starts_playing_a_song())

        # Otherwise, add the song to queue
        elif not override:
            await vc.queue.put_wait(query)
            await interaction.response.send_message(respond.add_song_to_queue())

            # Prepares an embed message
            embed: Embed = Embed(
                title="Song added to queue!",
                description=vc.current.title,
                color=Color.random()
            )
            embed.add_field(
                name="Author:",
                value=vc.current.author
            )
            embed.add_field(
                name="Duration:",
                value=Music.convert_duration(vc.current.duration)
            )
            embed.set_thumbnail(f"https://img.youtube.com/vi/{vc.current.identifier}/default.jpg")

            # Sends the embed message
            channel = self.bot.get_channel(api.fetch_command_channel(interaction.guild_id))
            await channel.send(embed=embed)

    # Skip command
    @nextcord.slash_command(guild_ids=[], description="Have Cosette to cue up the next melody in line.")
    async def skip(self, interaction: Interaction) -> None:

        # Initializes Wavelink Player
        vc: wavelink.Player = interaction.guild.voice_client

        # Have Cosette stop the current song. The whole thing is set so that
        # it automatically plays the next song if the current one is stopped
        try:
            if not vc.queue.is_empty:
                await interaction.response.send_message(respond.skip_song())
                await vc.stop()

            # If there are no more songs in the queue
            else:
                await interaction.response.send_message(respond.no_more_songs())

        # Exception handling: If the 'queue' object is not initialized
        # Presumed cause: there are no more songs
        except ApplicationInvokeError as e:
            await interaction.response.send_message(respond.no_more_songs())

    # Pause command
    @nextcord.slash_command(guild_ids=[], description="Give Cosette a breather - even music bots need a quick break.")
    async def pause(self, interaction: Interaction) -> None:

        # Initializes Wavelink Player
        vc: wavelink.Player = interaction.guild.voice_client

        try:
            # If Cosette is currently playing a song, have her pause it now
            if not vc.is_paused():
                await vc.pause()

                # Have her tell the user that the song is paused
                await interaction.response.send_message(respond.pause())

                # Prepares an embed message
                embed: Embed = Embed(
                    title="Song paused!",
                    description=vc.current.title,
                    color=Color.random()
                )
                embed.add_field(
                    name="Author:",
                    value=vc.current.author
                )
                embed.add_field(
                    name="Duration:",
                    value=Music.convert_duration(vc.current.duration)
                )
                embed.set_thumbnail(f"https://img.youtube.com/vi/{vc.current.identifier}/default.jpg")

                # Sends the embed message
                channel = self.bot.get_channel(api.fetch_command_channel(interaction.guild_id))
                await channel.send(embed=embed)

            # Otherwise, have her tell the user that she's not playing anything
            else:
                await interaction.response.send_message(respond.song_already_paused())

        # Exception handler: When the bot is not in a voice channel
        except Exception as e:
            await interaction.response.send_message(respond.no_song())

    # Resume command
    @nextcord.slash_command(guild_ids=[], description="Get the music flowing again! Cosette's tunes can't stay quiet for long.")
    async def resume(self, interaction: Interaction) -> None:

        # Initializes Wavelink Player
        vc: wavelink.Player = interaction.guild.voice_client

        try:
            # If the current song is indeed being paused
            if vc.is_paused():

                # Have Cosette resumes it
                await vc.resume()

                # Have her tell the user that the song is already playing
                await interaction.response.send_message(respond.resume_song())
                
                # Prepares an embed message
                embed: Embed = Embed(
                    title="Song resumed!",
                    description=vc.current.title,
                    color=Color.random()
                )
                embed.add_field(
                    name="Author:",
                    value=vc.current.author
                )
                embed.add_field(
                    name="Duration:",
                    value=Music.convert_duration(vc.current.duration)
                )
                embed.set_thumbnail(f"https://img.youtube.com/vi/{vc.current.identifier}/default.jpg")

                # Sends the embed message
                channel = self.bot.get_channel(api.fetch_command_channel(interaction.guild_id))
                await channel.send(embed=embed)

            # Otherwise, have her tell the user that the song is already resumed
            else:
                await interaction.response.send_message(respond.song_already_resumed())

        # Exception handler: When the bot is not in a voice channel
        except Exception as e:
            await interaction.response.send_message(respond.no_song())

    # Stop command
    @nextcord.slash_command(guild_ids=[], description="Hush Cosette's melodious purrs, leaving her song unfinished.")
    async def stop(self, interaction: Interaction) -> None:

        # Initializes Wavelink Player
        vc: wavelink.Player = interaction.guild.voice_client

        try:
            # Have Cosette disconnects from the voice channel
            await vc.disconnect()

            # Have Cosette tells the user a message as she leaves the voice channel
            await interaction.response.send_message(respond.leave_voice_channel())

            # Have Cosette clears the music player queue
            if not vc.queue.is_empty:
                await vc.queue.clear()
                
            # Prepares an embed message
            embed: Embed = Embed(
                title="Song stopped!",
                description="Playlist has been cleared!",
                color=Color.random()
            )

            # Sends the embed message
            channel = self.bot.get_channel(api.fetch_command_channel(interaction.guild_id))
            await channel.send(embed=embed)

        # Exception handling: If Cosette is not even in a voice channel
        except ApplicationInvokeError as e:

            pass    # TODO: Have her tease the user

    # See queue command
    @nextcord.slash_command(guild_ids=[], description="Peek into Cosette's song queue.")
    async def queue(self, interaction: Interaction) -> None:

        # Initializes Wavelink Player
        vc: wavelink.Player = interaction.guild.voice_client

        try:
            # If the queue is not empty
            if vc.is_playing():

                # Have Cosette say something first
                # await interaction.response.send_message(respond.show_queue())

                # Setup an embed message
                embed: Embed = Embed(title="Current Playlist", color=Color.random())
                embed.set_thumbnail(f"https://img.youtube.com/vi/{vc.current.identifier}/default.jpg")

                # Include the song that is currently playing to the embed message
                embed.add_field(
                    name="Now playing:",
                    value=f"{ vc.current.title } — ({ Music.convert_duration(vc.current.duration) })"
                )

                # If there are more songs in the queue
                if not vc.queue.is_empty:

                    # Counts how many songs are in the queue
                    song_counter: int = 0

                    # Lists all the songs in the queue to be added to the embed message
                    queue = vc.queue.copy()
                    songs: str = ""

                    for song in queue:
                        song_counter += 1
                        songs += f"\n {song_counter}. {song.title} — ({ Music.convert_duration(song.duration) })"

                    # Include the list of queued songs to the embed message
                    embed.add_field(
                        name="Queued songs:",
                        value=songs,
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

    # Automatically tells the name of the current song that is playing
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackEventPayload) -> None:

        # Prepares an embed message
        embed: Embed = Embed(
            title="Now playing:",
            description=payload.player.current.title,
            color=Color.random()
        )
        embed.add_field(
            name="Author:",
            value=payload.player.current.author
        )
        embed.add_field(
            name="Duration:",
            value=Music.convert_duration(payload.player.current.duration)
        )
        embed.set_footer(text=f"⏸ Pause  |  ⏹ Stop  {'| ⏭ Next song' if payload.player.queue else ''}")
        embed.set_thumbnail(f"https://img.youtube.com/vi/{payload.player.current.identifier}/default.jpg")
        
        # If there is a song in the queue, display the next song title
        if payload.player.queue:
            embed.add_field(
                name="Next:",
                value=f"{payload.player.queue[0].title} ({ Music.convert_duration(payload.player.queue[0].duration) })",
                inline=False
            )

        # Creates UI Buttons
        player_button_view = nextcord.ui.View()

        # Pause button
        async def pause_callback(interaction: Interaction, message: Message) -> None:
            vc: wavelink.Player = interaction.guild.voice_client
            global embed, player_button_view
            message.edit(embed=Embed, view=View)
        
        if not payload.player.is_paused():
            player_button_view.add_item(
                Button(
                    style=ButtonStyle.green,
                    label="Pause",
                    custom_id="pause",
                    emoji="⏸"
                ).callback(await self.pause)
            )
        
        # Resume button
        else:
            player_button_view.add_item(
                Button(
                    style=ButtonStyle.green,
                    label="Resume",
                    custom_id="resume",
                    emoji="▶"
                ).callback(await self.resume)
            )

        # Stop button
        player_button_view.add_item(
            Button(
                style=ButtonStyle.red,
                label="Stop",
                custom_id="stop",
                emoji="⏹"
            ).callback(await self.stop)
        )

        # Skip button (Only if there is a song in the queue)
        if payload.player.queue:
            player_button_view.add_item(
                Button(
                    style=ButtonStyle.grey,
                    label="Skip",
                    custom_id="skip",
                    emoji="⏭"
                ).callback(await self.skip)
            )

        # Sends the embed message
        channel = self.bot.get_channel(api.fetch_command_channel(payload.player.guild.id))
        msg: Message = await channel.send(embed=embed, view=player_button_view)

    # Converts milliseconds to a time string that is human-readable
    @staticmethod
    def convert_duration(milliseconds: int) -> str:

        # Convert milliseconds to seconds and remaining milliseconds
        seconds, milliseconds = divmod(milliseconds, 1000)

        # Convert seconds to minutes and remaining seconds
        minutes, seconds = divmod(seconds, 60)

        # Convert minutes to hours and remaining minutes
        hours, minutes = divmod(minutes, 60)

        # Prepares a string to store the output
        duration: str = ""

        # Include hours in the duration if the duration is longer than an hour
        if hours > 0:
            duration = f"{hours:02d}:"

        # Append minutes and seconds to the duration string
        duration += f"{minutes:02d}:{seconds:02d}"

        return f"`{duration}`"

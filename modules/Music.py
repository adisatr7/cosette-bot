from discord import Member, ButtonStyle, Color, Embed, ApplicationContext, Message, TextChannel, SelectOption, Option
from discord.errors import ApplicationCommandInvokeError
from discord.ui import Button, Select, View
from discord.ext import commands
import discord
import wavelink
import modules.ResponseVariety as respond
import api.controllers as api


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        print("Music cog loaded successfully!")

    # Play music command | TODO: Add Spotify support
    @discord.slash_command(name="play", description="Summon Cosette and let her work her magic with a YouTube jam")
    async def play(
        self,
        ctx: ApplicationContext,
        search_keyword: str = Option(
            str,
            description="Enter the search query or YouTube URL of the song you want to play",
            required=True
        ),
        override: bool = Option(
            bool,
            description="Play the new song immediately, replacing the one currently playing (optional)",
            required=False,
            default=False)
    ) -> None:

        # Debugging purposes
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /play from channel ID {ctx.channel_id}")

        # Remembers which text channel the command is executed from
        api.active_channel.set(ctx.guild_id, ctx.channel_id)

        # Do a YouTube search
        query = await wavelink.Playable.search(search_keyword)
        print(f"Searching for song {query[0].title} with ID {query[0].identifier}")

        # Set the target voice channel where the user is in
        try:
            destination = ctx.user.voice.channel

        # Exception handler: If the user is not in a voice channel
        # TODO: Test what happens if the user is in a voice channel that she has no permission to join
        except AttributeError as e:
            # Have Cosette respond to them via chat
            await ctx.response.send_message(respond.user_not_in_voice_channel())
            # End the function early
            return

        # If Cosette is not already in the voice channel, have her join one now
        if not ctx.guild.voice_client:
            player: wavelink.Player = await destination.connect(cls=wavelink.Player)

        # If the user is in another channel, have Cosette move there
        elif ctx.guild.voice_client.channel != destination:
            player: wavelink.Player = await ctx.guild.voice_client.move_to(destination)
            await ctx.response.send_message(respond.move_to_different_vc())

        # Otherwise, stay there
        else:
            player: wavelink.Player = ctx.guild.voice_client

        # If the queue is empty and the player is not playing, have Cosette play the song now
        if override or not player.playing:
            await player.play(query[0])
            if player.paused:
                await player.pause()
            msg: Message = await ctx.response.send_message(respond.starts_playing_a_song())

            # Remembers where active channel is
            guild_id = ctx.guild_id
            channel_id = ctx.channel_id
            api.active_channel.set(guild_id, channel_id)

            # Remove any player buttons from the previous message
            if override:
                await self.__remove_player_buttons(player)

        # Otherwise, add the song to queue
        elif not override:
            await player.queue.put_wait(query[0])
            await ctx.response.send_message(respond.add_song_to_queue())

            # Remove any player buttons from the previous message
            # await self.__remove_player_buttons(player)

            # Update the buttons in the previous message
            await self.__remove_player_buttons(player)
            buttons: View = self.__render_player_buttons(player)

            # Get the ID of the message where the buttons are attached to
            msg_id, ch_id = api.message_buttons.get(ctx.guild_id)
            ch = self.bot.get_channel(ch_id)
            msg = await ch.fetch_message(msg_id)

            # Update the buttons and embed
            embed = self.__render_embed("Now playing:", player)
            await msg.edit(embed=embed, view=buttons)

            # Prepares an embed message
            embed: Embed = Embed(
                title="Song added to queue!",
                description=query[0].title,
                color=Color.random()
            )
            embed.add_field(
                name="Author:",
                value=query[0].author
            )
            embed.add_field(
                name="Duration:",
                value=Music.convert_duration(query[0].length)
            )
            embed.set_thumbnail(url=f"https://img.youtube.com/vi/{query[0].identifier}/default.jpg")

            # Attach player buttons to this new message
            # buttons: View = self.__render_player_buttons(player)

            # Sends the embed message
            await ctx.channel.send(embed=embed)

        # EXPERIMENTAL
        # api.queue_controller.set(ctx.guild_id, player.queue)
        # api.queue_controller.clear(ctx.guild_id)
        # debug: wavelink.Queue = api.queue_controller.get(ctx.guild_id)
        # print(f"DEBUG: Real queue output test: {player.queue}")
        # print(f"DEBUG: Firestore queue test: {debug}")

    # Skip command
    @discord.slash_command(name="skip", description="Have Cosette to cue up the next melody in line.")
    async def skip(self, ctx: ApplicationContext) -> None:
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /skip from channel ID {ctx.channel_id}")
        await self.__skip_callback(ctx, True)

    # Pause command
    @discord.slash_command(name="pause", description="Give Cosette a breather - even music bots need a quick break.")
    async def pause(self, ctx: ApplicationContext) -> None:
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /pause from channel ID {ctx.channel_id}")
        await self.__pause_callback(ctx, True)

    # Resume command
    @discord.slash_command(name="resume", description="Get the music flowing again! Cosette's tunes can't stay quiet for long.")
    async def resume(self, ctx: ApplicationContext) -> None:
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /resume from channel ID {ctx.channel_id}")
        await self.__resume_callback(ctx, True)

    # Stop command
    @discord.slash_command(name="stop", description="Hush Cosette's melodious purrs, leaving her song unfinished.")
    async def stop(self, ctx: ApplicationContext) -> None:
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /stop from channel ID {ctx.channel_id}")
        await self.__stop_callback(ctx, True)

    # See queue command
    @discord.slash_command(name="queue", description="Peek into Cosette's song queue.")
    async def queue(self, ctx: ApplicationContext) -> None:
        print(f"User {ctx.user.display_name} of guild ID {ctx.guild_id} called /queue from channel ID {ctx.channel_id}")

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        try:
            # If the queue is not empty
            if player.playing:

                # Have Cosette say something first
                # await ctx.response.send_message(respond.show_queue())

                # Setup an embed message
                embed: Embed = Embed(title="Current Playlist", color=Color.random())
                embed.set_thumbnail(url=f"https://img.youtube.com/vi/{player.current.identifier}/default.jpg")

                # Include the song that is currently playing to the embed message
                embed.add_field(
                    name="Now playing:",
                    value=f"{ player.current.title } — ({ Music.convert_duration(player.current.duration) })",
                    inline=False
                )
                embed.add_field(
                    name="Author:",
                    value=player.current.author
                )
                embed.add_field(
                    name="Duration:",
                    value=Music.convert_duration(player.current.duration)
                )
                embed.add_field(
                    name="Loop mode:",
                    value=f"`{api.loop_mode.get(player.guild.id)}`"
                )
                embed.add_field(
                    name="Shuffle mode:",
                    value="`To be added soon!`"    # f"`{api.shuffle_mode.get(player.guild.id)}`"
                )

                # If there are more songs in the queue
                if not player.queue.is_empty:

                    # Remove player buttons that are currently attached to an embed message
                    await self.__remove_player_buttons(player)

                    # Counts how many songs are in the queue
                    song_counter: int = 0

                    # Lists all the songs in the queue to be added to the embed message
                    queue = player.queue.copy()
                    songs: str = ""

                    for song in queue:
                        song_counter += 1
                        if song == player.current:
                            songs += f"\n**{song_counter}. {song.title} — ({ Music.convert_duration(song.duration)}) (Now playing)**"
                        else:
                            songs += f"\n{song_counter}. {song.title} — ({ Music.convert_duration(song.duration)})"

                    # Include the list of queued songs to the embed message
                    embed.add_field(
                        name="Queued songs:",
                        value=songs,
                        inline=False
                    )

                # Prepare new buttons to be attached to this new embed message
                buttons = self.__render_player_buttons(player)

                # Send the embed message containing queue data to the user
                await ctx.response.send_message(embed=embed, view=buttons)

            # If the queue is empty
            else:

                # Have Cosette tells the user that the queue is indeed empty
                await ctx.response.send_message(respond.queue_is_empty())

        # Exception handler: If the 'queue' object is not initialized
        except AttributeError as e:

            # Have Cosette tells the user that she's not playing anything at the moment
            await ctx.response.send_message(respond.queue_is_empty())

    # Automatically have Cosette do something when a song is over
    # @commands.Cog.listener()
    # async def on_wavelink_track_end(self, payload: wavelink.Playable) -> None:

    # Automatically tells the name of the current song that is playing
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.Playable) -> None:

        player: wavelink.Player = payload.player

        # Removes the buttons from the previous message
        await self.__remove_player_buttons(payload.player)

        # Prepares an embed message
        embed: Embed = self.__render_embed(header="Now playing:", player=player)

        # Initializes player buttons
        buttons = self.__render_player_buttons(player=player)

        # Sends the embed message
        channel_id: int = api.active_channel.get(player.guild.id)
        channel: TextChannel = self.bot.get_channel(channel_id)
        msg: Message = await channel.send(embed=embed, view=buttons)

        # Remembers where the last message with buttons is
        api.message_buttons.set(player.guild.id, msg.id)

    async def __pause_callback(self, ctx: ApplicationContext, reaction: bool = False) -> None:
        """Pauses the current song."""

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        try:
            # If Cosette is currently playing a song
            if not player.paused:

                # Remove any player buttons from the previous message
                await self.__remove_player_buttons(player)

                # Pause the player
                await player.pause()

                # Have her tell the user that the song is paused
                # if reaction:
                await ctx.response.send_message(respond.pause())

                # Prepares an embed message
                embed: Embed = self.__render_embed(header="Song paused!", player=player)

                # Attach player buttons to this new message
                buttons: View = self.__render_player_buttons(player)

                # Sends the embed message
                channel = self.bot.get_channel(api.active_channel.get(ctx.guild_id))
                msg = await channel.send(embed=embed, view=buttons)

                # Remembers where the last message with buttons is
                api.message_buttons.set(ctx.guild_id, msg.id)

            # Otherwise, have her tell the user that she's not playing anything
            else:
                await ctx.response.send_message(respond.song_already_paused())

        # Exception handler: When the bot is not in a voice channel
        except Exception as e:
            await ctx.response.send_message(respond.no_song_playing())

    async def __resume_callback(self, ctx: ApplicationContext, reaction: bool = False) -> None:

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        try:
            # If the current song is indeed being paused
            if player.paused:

                # Remove any player buttons from the previous message
                await self.__remove_player_buttons(player)

                # Have Cosette resumes it
                await player.resume()

                # Have her tell the user that the song is already playing
                # if reaction:
                await ctx.response.send_message(respond.resume_song())

                # Prepares an embed message
                embed: Embed = self.__render_embed(header="Song resumed!", player=player)

                # Initializes player buttons
                buttons = self.__render_player_buttons(player)

                # Sends the embed message
                channel_id: int = api.active_channel.get(ctx.guild_id)
                channel = self.bot.get_channel(channel_id)
                msg = await channel.send(embed=embed, view=buttons)

                # Remembers where the last message with buttons is
                api.message_buttons.set(ctx.guild_id, msg.id)

            # Otherwise, have her tell the user that the song is already resumed
            else:
                print("Song is already resumed!")
                await ctx.response.send_message(respond.song_already_resumed())

        # Exception handler: When the bot is not in a voice channel
        except Exception as e:
            print("Failed: There is no song to begin with!")
            await ctx.response.send_message(respond.no_song_playing())

    async def __stop_callback(self, ctx: ApplicationContext, reaction: bool = False) -> None:
        """Stops the current song and clears the queue."""

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        try:
            # Remove any player buttons from the previous message
            await self.__remove_player_buttons(player)

            # Have Cosette disconnects from the voice channel
            await player.disconnect()

            # Have Cosette tells the user a message as she leaves the voice channel
            vc_members: list[Member] = ctx.user.voice.channel.members

            # If there are more than 1 users in the voice channel
            if len(vc_members) > 1:
                # Have Cosette expresses disappointment, sadness, or annoyance
                await ctx.response.send_message(respond.leave_vc_mid_performance())

            # If she's the only one left in the voice channel
            else:
                # Have Cosette thanks the user for having her
                await ctx.response.send_message(respond.leave_vc_no_users())

            # Have Cosette clears the music player queue
            # if not player.queue.is_empty:
            #     await player.queue.clear()

            # Prepares an embed message
            embed: Embed = Embed(
                title="Song stopped!",
                description="Playlist has been cleared!",
                color=Color.random()
            )

            # Sends the embed message
            channel_id: int = api.active_channel.get(ctx.guild_id)
            channel: TextChannel = self.bot.get_channel(channel_id)
            msg: TextChannel = await channel.send(embed=embed)

            # Remembers where the last message with buttons is
            api.message_buttons.set(ctx.guild_id, msg.id)

        # Exception handling: If Cosette is not even in a voice channel
        except ApplicationCommandInvokeError as e:
            await ctx.response.send_message(respond.already_stopped())

    async def __skip_callback(self, ctx: ApplicationContext, reaction: bool = False) -> None:
        """Skips the current song and plays the next one in queue."""

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        # Have Cosette stop the current song. The whole thing is set so that
        # it automatically plays the next song if the current one is stopped
        try:
            if not player.queue.is_empty:
                await self.__remove_player_buttons(player)
                await player.stop()

                # if reaction:
                await ctx.response.send_message(respond.skip_song())

            # If there are no more songs in the queue
            else:
                await ctx.response.send_message(respond.no_more_songs())

        # Exception handling: If the 'queue' object is not initialized
        # Presumed cause: there are no more songs in the queue
        except ApplicationCommandInvokeError and AttributeError as e:
            await ctx.response.send_message(respond.no_more_songs())

    def __render_embed(self, header: str, player: wavelink.Player) -> Embed:

        track: wavelink.Playable = player.current

        # Prepares an embed message
        embed: Embed = Embed(
            title=header,
            description=track.title,
            color=Color.random()
        )
        embed.add_field(
            name="Author:",
            value=track.author
        )
        embed.add_field(
            name="Duration:",
            value=Music.convert_duration(track.length)
        )
        embed.add_field(
            name="Loop mode:",
            value=f"`{api.loop_mode.get(player.guild.id)}`"
        )
        embed.add_field(
            name="Shuffle mode:",
            value="`To be added soon!`"    # f"`{api.shuffle_mode.get(player.guild.id)}`"
        )
        embed.set_thumbnail(url=f"https://img.youtube.com/vi/{track.identifier}/default.jpg")

        # If there is a song in the queue, display the next song title
        try:
            if not player.queue.is_empty:
                embed.add_field(
                    name="Next:",
                    value=f"{player.queue[0].title} ({ Music.convert_duration(player.queue[0].length) })",
                    inline=False
                )

        except IndexError or wavelink.QueueEmpty as e:
            pass

        return embed

    def __render_player_buttons(self, player: wavelink.Player) -> View:

        # Creates the view for the buttons
        player_buttons_view = View(timeout=player.current.length / 1000)
        # player_buttons_view.on_timeout = lambda: self.__remove_player_buttons(player)

        # Pause button
        if not player.paused:
            pause_button = Button(
                style=ButtonStyle.blurple,
                label="Pause",
                custom_id="pause",
            )
            pause_button.callback = self.__pause_callback
            player_buttons_view.add_item(pause_button)

        # Resume button
        else:
            resume_button = Button(
                style=ButtonStyle.blurple,
                label="Resume",
                custom_id="resume",
            )
            resume_button.callback = self.__resume_callback
            player_buttons_view.add_item(resume_button)

        # Skip button (Only if there is a song in the queue)
        if player.queue:
            skip_button = Button(
                style=ButtonStyle.blurple,
                label="Skip",
                custom_id="skip",
            )
            skip_button.callback = self.__skip_callback
            player_buttons_view.add_item(skip_button)

        # Stop button
        stop_button = Button(
            style=ButtonStyle.red,
            label="Stop",
            custom_id="stop"
        )
        stop_button.callback = self.__stop_callback
        player_buttons_view.add_item(stop_button)

        loop_settings = Select(
            placeholder="Loop settings",
            options=[
                SelectOption(label="off", value="off", description="Disable looping"),
                SelectOption(label="single", value="single", description="Set the current song on loop"),
                SelectOption(label="all", value="all", description="Set the whole queue on loop")
            ],
            min_values=1,
            max_values=1
        )
        loop_settings.callback = lambda ctx: self.__loop_settings_callback(ctx, loop_settings)
        player_buttons_view.add_item(loop_settings)

        # TODO: Loop button, jump button, shuffle button

        return player_buttons_view

    async def __remove_player_buttons(self, player: wavelink.Player) -> None:

        # Fetch the message ID & channel ID where the buttons are attached to from Firestore
        msg_id, channel_id = api.message_buttons.get(player.guild.id)

        # If there is a message ID
        if msg_id > 0:

            # Fetch the channel where the buttons are attached to
            channel: TextChannel = self.bot.get_channel(channel_id)

            # Fetch the message where the buttons are attached to
            msg: Message = await channel.fetch_message(msg_id)

            # Update the buttons
            await msg.edit(embed=msg.embeds[0], view=None)

            # Clear the message ID from Firestore
            api.message_buttons.clear(player.guild.id)

    async def __loop_settings_callback(self, ctx: ApplicationContext, dropdown: Select) -> None:
        """Handles the loop settings."""

        # Initializes Wavelink Player
        player: wavelink.Player = ctx.guild.voice_client

        # If the user selects "off"
        if dropdown.values[0] == "off":
            player.queue.loop = False
            player.queue.loop_all = False
            api.loop_mode.set(player.guild.id, "off")

        # If the user selects "single"
        elif dropdown.values[0] == "single":
            player.queue.loop = True
            player.queue.loop_all = False
            api.loop_mode.set(player.guild.id, "single")

        # If the user selects "all"
        elif dropdown.values[0] == "all":
            player.queue.loop = False
            player.queue.loop_all = True
            api.loop_mode.set(player.guild.id, "all")

        # Update the buttons and embed
        await self.__remove_player_buttons(player)

        embed = self.__render_embed("Now playing:", player)
        buttons = self.__render_player_buttons(player)
        await ctx.message.edit(embed=embed, view=buttons)

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

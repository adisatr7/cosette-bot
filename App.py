# Import necessary libraries
import discord
import modules.ResponseVariety as respond
import wavelink
import os
from dotenv import load_dotenv
from discord.ext import commands
from constants.prefixes import COMMAND_PREFIXES
from modules.Music import Music
from modules.DiceRoll import DiceRoll


# Declare Cosette's permissions
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True

# Initializes Cosette
bot: commands.Bot = commands.Bot(
    command_prefix=COMMAND_PREFIXES,
    intents=intents
)

# Import cogs from ./modules folder
bot.add_cog(Music(bot))
bot.add_cog(DiceRoll(bot))


# Setting up wavelink node for Cosette's music player function
async def on_node():
    node: wavelink.Node = wavelink.Node(
        uri=str(os.getenv("WAVELINK_URI")),
        password=str(os.getenv("WAVELINK_PASSWORD"))
    )
    await wavelink.Pool.connect(client=bot, nodes=[node])
    wavelink.Player.autoplay = True


# When Cosette is just started up
@bot.event
async def on_ready() -> None:

    # Declare Cosette's activity status
    activity = discord.Activity(
        name="to you",
        type=discord.ActivityType.listening
    )

    # Actually change the activity status
    await bot.change_presence(activity=activity)

    # Have Cosette send a greeting to the console
    print(f"{ respond.come_online() } \n")

    # Have Cosette connects to a node for her music player to function correctly
    bot.loop.create_task(on_node())


# When the Cosette receives a message in any channels she's in
@bot.event
async def on_message(message: discord.Message or None) -> None:

    # If Cosette is mentioned without further context, have her respond randomly
    if bot.user.mentioned_in(message):

        # Console log user's message
        print(f"{message.author}: \"{message.content}\"")

        # Have her respond to the chat
        await message.channel.send(respond.respond_to_mention())


# Keep Cosette up and running by looping this whole process
load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))

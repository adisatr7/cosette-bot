# Import necessary libraries
import nextcord
import modules.response_variety as respond
import wavelink
import re
from random import randint
from nextcord.ext import commands
from typing import Literal
from constants.prefixes import COMMAND_PREFIXES
from modules.music import Music
from modules.diceroll import DiceRoll


# Declare Cosette's permissions
intents = nextcord.Intents.default()
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


# Keep Cosette up and running by looping this whole process
bot.run("MTExNDIyMTM3NDc4NTk4MjUxNA.GlMPuw.dZyNhpd3e5QVeJSP0KDz80lQSmUzByORdAzBQ4")

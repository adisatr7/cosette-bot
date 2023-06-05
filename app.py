# Import necessary libraries
import nextcord
import modules.response_variety as respond
import wavelink
import re
from random import randint
from nextcord.ext import commands
from typing import List, Literal
from constants.prefixes import COMMAND_PREFIXES
from modules.music import Music


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
extensions: List[str] = [
    "modules.music"
]
bot.load_extensions(extensions)

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
        output = f"**({rolled})**" if rolled == max_roll or rolled == 1 else f"({rolled})"

    # Send the roll result to the user
    await interaction.response.send_message(respond.rolling_dice())
    await interaction.channel.send(f"🎲 {amount or 1}{die_type} = { output }")


# Keep Cosette up and running by looping this whole process
bot.run("MTExNDIyMTM3NDc4NTk4MjUxNA.GlMPuw.dZyNhpd3e5QVeJSP0KDz80lQSmUzByORdAzBQ4")

# Import necessary libraries
import nextcord
import modules.chat as chat
from nextcord.ext import commands
from constants.prefixes import COMMAND_PREFIXES


# Declare Cosette's permissions
intents = nextcord.Intents.default()
intents.message_content = True
intents.presences = True

# Initializes Cosette
bot: commands.Bot = commands.Bot(command_prefix=COMMAND_PREFIXES, intents=intents)


# When Cosette is started up
@bot.event
async def on_ready() -> None:

    # Declare Cosette's activity status
    activity = nextcord.Activity(
        name="to you",
        type=nextcord.ActivityType.listening
    )

    # Actually change the activity status
    await bot.change_presence(activity=activity)

    # Console log
    print(f"{chat.come_online()} \n")


# When the Cosette receives a message in any channels she's in
@bot.event
async def on_message(message: nextcord.message or None) -> None:

    # If Cosette is mentioned
    if bot.user.mentioned_in(message):
        response = chat.respond_to_mention()
        await message.channel.send(response)


bot.run("MTExNDIyMTM3NDc4NTk4MjUxNA.GlMPuw.dZyNhpd3e5QVeJSP0KDz80lQSmUzByORdAzBQ4")

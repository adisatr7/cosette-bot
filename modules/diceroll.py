import re
import nextcord
import modules.response_variety as respond
from nextcord.ext import commands
from random import randint
from typing import Literal


class DiceRoll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("DiceRoll cog loaded successfully!")

    # Roll dice command
    @nextcord.slash_command(guild_ids=[], description="Have Cosette roll various dice for you TTRPG nerds.")
    async def roll(
        self,
        interaction: nextcord.Interaction,
        die_type: Literal['d20', 'd12', 'd10', 'd100', 'd8', 'd6', 'd4', 'd2'] = nextcord.SlashOption(description="Choose the die type."),
        amount: int | None = nextcord.SlashOption(min_value=1, description="Set how many dice you want to roll. Defaults to 1 if left empty.")
    ) -> None:

        # Sets the max roll based on the die type used
        max_roll: int = int(re.findall(r"\d+", die_type)[0])

        # Prepares a variable named 'result' that can be an Integer or String
        rolled: int = 0

        # Prepares a variable named 'output' for the output, duh~
        output: str = ""

        # If user asks for multiple dice to be rolled
        if amount is not None and amount > 1:

            # Prepares a list of numbers to store all the results
            results: list[str] = []

            # Prepares an integer to store the total value of all rolls
            total: int = 0

            # Do the rolling
            for i in range(amount):
                rolled = randint(1, max_roll)
                total += rolled

                # Bold the result if it's a nat 1 or nat max
                if rolled == max_roll or rolled == 1:

                    # Append the roll result into the list of results
                    results.append(f"**{rolled}**")

                else:
                    results.append(f"{rolled}")

            output = f"({ ', '.join(results) }) \n**Total:** {total}"

        # If user asks for a single roll
        else:
            rolled = randint(1, max_roll)

            # Bold the result if it's a nat 1 or nat max
            output = f"**({rolled})**" if rolled == max_roll or rolled == 1 else f"({rolled})"

        # Send the roll result to the user
        await interaction.response.send_message(respond.rolling_dice())
        await interaction.channel.send(f"🎲 **Rolling:** {amount or 1}{die_type} = { output }")

        # Prepares an embed message
        # embed: nextcord.Embed = nextcord.Embed(
        #     title="Dice Roller",
        #     color=nextcord.Color.random()
        # )
        # embed.add_field(
        #     name="Rolling:",
        #     value=f"🎲 {amount or 1}{die_type}"
        # )
        # embed.add_field(
        #     name="Result:",
        #     value=output
        # )

        # Sends the embed message
        # await interaction.channel.send(embed=embed)

import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class KeySystemView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Get Key", style=discord.ButtonStyle.green)
    async def get_key(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is your key!", ephemeral=True)

    @discord.ui.button(label="Booster", style=discord.ButtonStyle.blurple)
    async def booster(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Booster perks info!", ephemeral=True)

    @discord.ui.button(label="Lifetime", style=discord.ButtonStyle.red)
    async def lifetime(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Lifetime info!", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def panel(ctx):
    view = KeySystemView()
    await ctx.send("Click a button below:", view=view)

bot.run(os.getenv("DISCORD_TOKEN"))

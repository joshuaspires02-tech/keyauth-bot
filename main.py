import os
import discord
from discord.ext import commands
from discord.ui import Button, View
from threading import Thread
from flask import Flask

# 1. Setup Flask to keep Render happy
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Setup Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Define the interactive buttons
class KeySystemView(View):
    @discord.ui.button(label="Get Key", style=discord.ButtonStyle.primary)
    async def get_key(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("Here is your link to get the key!", ephemeral=True)

    @discord.ui.button(label="Reset HWID", style=discord.ButtonStyle.secondary)
    async def reset_hwid(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("Your HWID has been reset!", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Command to send the key system embed and buttons
@bot.command()
async def keysystem(ctx):
    embed = discord.Embed(
        title="Key System",
        description="Press **Get Key** to create a 72-hour key.",
        color=discord.Color.blurple()
    )
    await ctx.send(embed=embed, view=KeySystemView())

# 3. Run both Flask and the Bot
if __name__ == "__main__":
    keep_alive()
    TOKEN = os.environ.get("DISCORD_TOKEN")
    bot.run(TOKEN)

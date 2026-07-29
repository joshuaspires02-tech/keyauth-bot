import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class KeySystemView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Get Key", style=discord.ButtonStyle.primary, custom_id="get_key_btn")
    async def get_key(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Click the ad link to complete your key generation process!", ephemeral=True)

    @discord.ui.button(label="Booster", style=discord.ButtonStyle.danger, custom_id="booster_btn")
    async def booster(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Check server perks for booster rewards!", ephemeral=True)

    @discord.ui.button(label="Lifetime", style=discord.ButtonStyle.secondary, url="https://yourlink.com", custom_id="lifetime_btn")
    async def lifetime(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass # URL buttons handle links automatically

    @discord.ui.button(label="Reset HWID", style=discord.ButtonStyle.grey, custom_id="reset_hwid_btn")
    async def reset_hwid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Your HWID reset request has been processed.", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def panel(ctx):
    embed = discord.Embed(
        title="Key System",
        description=(
            "Press **get key** to create a 72 hour key.\n"
            "Once created, open the ad link and complete the process.\n"
            "The embed will update automatically once the key is completed.\n\n"
            "**Instructions**\n"
            "1. Press Get Key\n"
            "2. Complete the ads\n"
            "3. Receive your key.\n\n"
            "Press **lifetime** to skip the ads and purchase a key for `$19.99`"
        ),
        color=0x2b2d31
    )
    # Replace with your own banner image URL
    embed.set_image(url="https://your-image-url-here.png")
    
    view = KeySystemView()
    await ctx.send(embed=embed, view=view)

# Run the bot using your token from Render environment variables
bot.run(os.getenv("DISCORD_TOKEN"))

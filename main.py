import os
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f"Logged in as {client.user}")


class PersistentView(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(
      label="Get Key",
      style=discord.ButtonStyle.green,
      emoji="🔑",
      custom_id="get_key",
  )
  async def get_key_button(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    k = f"Joshua_hub{interaction.user.id}"
    await interaction.response.send_message(f"🔑 `{k}`", ephemeral=True)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # Type "!setup" in Discord to send the message with the button
  if message.content == "!setup":
    view = PersistentView()
    await message.channel.send("Click below to get your key:", view=view)


client.run(os.getenv("TOKEN"))

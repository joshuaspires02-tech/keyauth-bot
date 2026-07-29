import os
from threading import Thread
import discord
from flask import Flask

# Tiny web server to satisfy Render's port requirement
app = Flask('')


@app.route('/')
def home():
  return 'Bot is running!'


def run_web():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run_web)
  t.start()


# Discord Bot Setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'Logged in as {client.user}')


class PersistentView(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(
      label='Get Key',
      style=discord.ButtonStyle.green,
      emoji='🔑',
      custom_id='get_key',
  )
  async def get_key_button(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    k = f'Joshua_hub{interaction.user.id}'
    await interaction.response.send_message(f'🔑 `{k}`', ephemeral=True)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == '!setup':
    view = PersistentView()
    await message.channel.send('Click below to get your key:', view=view)


# Start web server and bot
if __name__ == '__main__':
  keep_alive()
  client.run(os.getenv('TOKEN'))

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
  await interaction.response.send_message(
      f"🔑 `{k}`", ephemeral=True
  )

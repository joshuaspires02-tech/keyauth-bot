@discord.ui.button(
    label="Get Key",
    style=discord.ButtonStyle.green,
    emoji="🔑",
    custom_id="get_key",
)
async def get_key_button(
    self, interaction: discord.Interaction, button: discord.ui.Button
):
  # 1. Generate or fetch the key for this specific user (interaction.user.id)
  user_id = interaction.user.id
  generated_key = f"Joshua_hub{user_id}"  # Replace this with your actual key generation logic or database query

  # 2. Send the key privately (ephemeral=True) so only they can see it
  await interaction.response.send_message(
      f"🔑 **Your Access Key:** `{generated_key}`\nStatus: Active & Verified\nInstructions: Copy the key above and paste it when prompted to unlock access.",
      ephemeral=True,
  )

import os
import discord
from discord.ext import commands
from datetime import datetime

# --------------------------
# 1️⃣ Setup Intents
# --------------------------
intents = discord.Intents.default()
intents.members = True          # REQUIRED for on_member_join
intents.message_content = False # Not needed unless you add commands

# --------------------------
# 2️⃣ Bot Setup
# --------------------------
bot = commands.Bot(command_prefix="!", intents=intents)

# --------------------------
# 3️⃣ Bot Ready Event
# --------------------------
@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user} (ID: {bot.user.id})")

# --------------------------
# 4️⃣ Welcome Event
# --------------------------
@bot.event
async def on_member_join(member):
    WELCOME_CHANNEL_ID = 1463019706746408960  # 🔁 Replace if needed

    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)

    # Fallback if channel not found
    if channel is None:
        for ch in member.guild.text_channels:
            if ch.permissions_for(member.guild.me).send_messages:
                channel = ch
                break

    if channel is None:
        print(f"❌ No valid channel in {member.guild.name}")
        return

    join_time = datetime.utcnow().strftime("%B %d, %Y at %H:%M UTC")

    embed = discord.Embed(
        title=f"Welcome Dasher {member.name}! 🎉",
        description=(
            "Welcome to **DealDash**!\n"
            "The place for easy foods & hot deals 🍔🔥"
        ),
        color=discord.Color.green()
    )

    embed.set_thumbnail(
        url=member.avatar.url if member.avatar else member.default_avatar.url
    )

    embed.set_footer(text=f"Joined on {join_time}")

    await channel.send(embed=embed)
    print(f"✅ Welcome sent for {member.name}")

# --------------------------
# 5️⃣ Run Bot (Railway Safe)
# --------------------------
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ DISCORD_TOKEN not found in environment variables")

bot.run(TOKEN)

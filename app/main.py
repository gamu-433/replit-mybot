from core.start import DBot
import discord
import os

from dotenv import load_dotenv
load_dotenv()

Token = os.environ['TOKEN']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Bot立ち上げ
DBot(
    token=Token,
    intents=discord.Intents.all()
).run()
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class CroissantGuy(commands.Bot) :
    async def setup_hook(self) :
        for extension in ['commands', 'events'] :
            await self.load_extension(f'cogs.{extension}')

intents = discord.Intents.all()
bot = CroissantGuy(command_prefix='!', intents=intents)

keep_alive()
bot.run(token=token)
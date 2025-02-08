import os
import discord
import json, random
from discord.ext import commands
<<<<<<< HEAD:trash/old_main.py
# from keep_alive import keep_alive
=======
from keep_alive import keep_alive
>>>>>>> d1dffe763f336615c37f5a03a5667d298e7c2bf6:main.py

# Get the token from the environment variable
intents = discord.Intents.all()
intents.message_content = True

# Link to json file
links = json.load(open("gifs.json"))

# Define bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Commands
@bot.command()
async def bonjour(ctx):
  await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def yell(ctx):
  await ctx.send("AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH !")

@bot.command()
async def gymyell(ctx):
  await ctx.send("GO TO THE GYM ! NOW !")

@bot.command(name="gif", aliases=["guillotine"])
async def gifs(ctx):
  await ctx.send(random.choice(links[ctx.invoked_with]))

@bot.event
async def on_message(message):
  if "cannibalism" in message.content :
    await message.channel.send("https://media.discordapp.net/attachments/1007598476504338465/1334936943368081539/20240922_123137.jpg?ex=679e5869&is=679d06e9&hm=207216826a61fc8cc4de1ba93552da95d0984dc5ce666acffa9415b8f222b006&=&format=webp")



# Run bot
token = os.environ['TOKEN_BOT']
<<<<<<< HEAD:trash/old_main.py
# keep_alive()
=======
keep_alive()
>>>>>>> d1dffe763f336615c37f5a03a5667d298e7c2bf6:main.py
bot.run(token)
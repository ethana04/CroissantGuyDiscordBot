import discord
from discord.ext import commands

token = ""
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

### Commands

@bot.command(name="bonjour")
async def bonjour(context):
  await context.send(f"Bonjour {context.author} !")


@bot.command()
async def decount(context, delai: int):
  await context.send("Ready in ...")
  for i in range(delai, 0, -1):
    await context.send(i)
  await context.send("GOOOOO !")


@bot.command(
  description="Repeats the text we give to it",
  brief="Repeats the text",
  help="More help",
  hidden=False
)
async def repete(context, *, message):
  """Repeats the text we give to it (docstring)"""
  await context.send(message)

@bot.command()
async def yell(ctx):
  await ctx.send("AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH !")

@bot.command()
async def gymyell(ctx):
  await ctx.send("GO TO THE GYM ! NOW !")


### Events

# @bot.event
# async def on_message(message):
#   if "cannibalism" in message.content :
#     await message.channel.send("https://media.discordapp.net/attachments/1007598476504338465/1334936943368081539/20240922_123137.jpg?ex=679e5869&is=679d06e9&hm=207216826a61fc8cc4de1ba93552da95d0984dc5ce666acffa9415b8f222b006&=&format=webp")



if __name__ == '__main__': 
  bot.run(token=token)
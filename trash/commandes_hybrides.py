import discord
from discord.ext import commands

token = ""
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

### Commands

@bot.hybrid_command()
async def bonjour(ctx):
  await ctx.send(f"Bonjour {ctx.author} !")


@bot.hybrid_command()
async def decount(context, delai: int):
  await context.send("Ready in ...")
  for i in range(delai, 0, -1):
    await context.send(i)
  await context.send("GOOOOO !")


@bot.hybrid_command()
async def yell(ctx):
  await ctx.send("AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH !")


@bot.hybrid_command()
async def gymyell(ctx):
  await ctx.send("GO TO THE GYM ! NOW !")

# ### Events

@bot.event
async def on_message(message):
  if message.author.bot:
    return
  else :
    if "cannibalism" in message.content :
      await message.channel.send("https://media.discordapp.net/attachments/1007598476504338465/1334936943368081539/20240922_123137.jpg?ex=679e5869&is=679d06e9&hm=207216826a61fc8cc4de1ba93552da95d0984dc5ce666acffa9415b8f222b006&=&format=webp")
    elif "tree" in message.content :
      await  message.channel.send("TREE ? Someone said tree ? <@1007600320001613887> \n The tree is here : <#1007660806118309961>")


@bot.event
async def on_ready():
  await bot.tree.sync()


### Launch

def main():
  bot.run(token = token)

if __name__ == '__main__':
  main()
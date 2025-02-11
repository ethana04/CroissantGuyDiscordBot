import json, random
from discord.ext import commands

# Link to json file
links = json.load(open("media/gifs.json"))

class CommmandsCog(commands.Cog):
  def __init__(self, bot) :
    self.bot = bot

  @commands.hybrid_command()
  async def bonjour(self, ctx) :
    await ctx.send(f"Bonjour {ctx.author} !")

  @commands.hybrid_command()
  async def decount(self, context, delai: int) :
    await context.send("Ready in ...")
    for i in range(delai, 0, -1):
      await context.send(i)
    await context.send("GOOOOO !")

  @commands.hybrid_command()
  async def yell(self, ctx) :
    await ctx.send("AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH !")

  @commands.hybrid_command()
  async def gymyell(self, ctx) :
    await ctx.send("GO TO THE GYM ! NOW !")

  @commands.hybrid_command(name="gif", aliases=["guillotine"])
  async def gifs(self, ctx) :
    await ctx.send(random.choice(links[ctx.invoked_with]))


async def setup(bot) :
  await bot.add_cog(CommmandsCog(bot))
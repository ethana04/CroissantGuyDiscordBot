import json, random
import discord
from discord.ext import commands
from embed import getDefaultEmbedColour

# Link to json file
links = json.load(open("media/gifs.json"))

class CommmandsCog(commands.Cog):
  def __init__(self, bot) :
    self.bot = bot

  @commands.hybrid_command()
  async def bonjour(self, ctx) :
    embed = discord.Embed(colour = getDefaultEmbedColour(), description=f"Bonjour {ctx.author} !")
    await ctx.send(embed=embed)

  @commands.hybrid_command()
  async def decount(self, context, delai: int) :
    embed = discord.Embed(colour = getDefaultEmbedColour(), description="Ready in ...")
    await context.send(embed=embed)
    for i in range(delai, 0, -1):
      embed = discord.Embed(colour = getDefaultEmbedColour(), description=i)
      await context.send(embed=embed)
    embed = discord.Embed(colour = getDefaultEmbedColour(), description="GOOOOO !")
    await context.send(embed=embed)

  @commands.hybrid_command()
  async def yell(self, ctx) :
    embed = discord.Embed(colour = getDefaultEmbedColour(), description="AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH !")
    await ctx.send(embed=embed)

  @commands.hybrid_command()
  async def gymyell(self, ctx) :
    embed = discord.Embed(colour = getDefaultEmbedColour(), description="GO TO THE GYM ! NOW !")
    await ctx.send(embed=embed)

  @commands.hybrid_command(name="gif", aliases=["guillotine"])
  async def gifs(self, ctx) :
    embed = discord.Embed(colour = getDefaultEmbedColour())
    embed.set_image(url=random.choice(links[ctx.invoked_with]))
    await ctx.send(embed=embed)


async def setup(bot) :
  await bot.add_cog(CommmandsCog(bot))
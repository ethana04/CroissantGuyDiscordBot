import discord
from discord.ext import commands
from embed import getDefaultEmbedColour

class EventsCog(commands.Cog) :
  def __init__(self, bot) :
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message) :
    if message.author.bot:
      return
    else :
      if (message.author.name == "suitcasewean" or message.author.name == "antlerhunter") and  "FRANCE" in message.content.upper():
        file1 = discord.File("media/miss_france.gif", filename="miss_france.gif")
        embed1 = discord.Embed(colour = getDefaultEmbedColour())
        embed1.set_image(url="attachment://miss_france.gif")
        await message.channel.send(file = file1, embed=embed1)
      if "CANNIBALISM" in message.content.upper() :
        file2 = discord.File("media/cannibalism.jpg", filename="cannibalism.jpg")
        embed2 = discord.Embed(colour = getDefaultEmbedColour())
        embed2.set_image(url="attachment://cannibalism.jpg")
        await message.channel.send(file = file2, embed=embed2)
      if "TREE" in message.content.upper() :
        embed3 = discord.Embed(colour = getDefaultEmbedColour(), title="TREE ?", description="Someone said tree ?  <@1007600320001613887>")
        embed3.add_field(name="", value="The tree is here : <#1007660806118309961>", inline=False)
        await  message.channel.send(embed=embed3)
      if "AHH" in message.content.upper() :
        embed4 = discord.Embed(colour = getDefaultEmbedColour(), title="AAAHHHHHHHHH", description="AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        await message.channel.send(embed=embed4)

async def setup(bot) :
  await bot.add_cog(EventsCog(bot))
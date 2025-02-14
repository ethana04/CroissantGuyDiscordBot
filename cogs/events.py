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
      if " TREE " in message.content.upper() :
        embed3 = discord.Embed(colour = getDefaultEmbedColour(), title="TREE ?", description="Someone said tree ?  <@1007600320001613887>")
        embed3.add_field(name="", value="The tree is here : <#1007660806118309961>", inline=False)
        await  message.channel.send(embed=embed3)
      if "AHH" in message.content.upper() :
        file4 = discord.File("media/goat.jpg", filename="goat.jpg")
        embed4 = discord.Embed(colour = getDefaultEmbedColour(), title="AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        # embed4.set_thumbnail(url="attachment://goat.jpg")
        # await message.channel.send(file=file4, embed=embed4)
        await message.channel.send(embed=embed4)
      if message.author.name == "suitcasewean" and  " ANANAS" in message.content.upper():
        file5 = discord.File("media/ananas.gif", filename="ananas.gif")
        embed5 = discord.Embed(colour = getDefaultEmbedColour())
        embed5.set_image(url="attachment://ananas.gif")
        await message.channel.send(file = file5, embed=embed5)
      if " OLA " in message.content.upper() :
        file6 = discord.File("media/nerd_face.jpg", filename="nerd_face.jpg")
        embed6 = discord.Embed(colour = getDefaultEmbedColour(), title="You spelled Hola wrong !")
        # embed6.set_image(url="attachment://nerd_face.jpg")
        # await message.channel.send(file=file6, embed=embed6)
        await message.channel.send(embed=embed6)

async def setup(bot) :
  await bot.add_cog(EventsCog(bot))
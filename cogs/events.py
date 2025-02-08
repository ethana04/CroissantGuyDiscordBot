import discord
from discord.ext import commands

class EventsCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return
    else :
      if "CANNIBALISM" in message.content.upper() :
        await message.channel.send("https://media.discordapp.net/attachments/1007598476504338465/1334936943368081539/20240922_123137.jpg?ex=679e5869&is=679d06e9&hm=207216826a61fc8cc4de1ba93552da95d0984dc5ce666acffa9415b8f222b006&=&format=webp")
      elif "TREE" in message.content.upper() :
        await  message.channel.send("TREE ? Someone said tree ? <@1007600320001613887> \n The tree is here : <#1007660806118309961>")


async def setup(bot):
  await bot.add_cog(EventsCog(bot))
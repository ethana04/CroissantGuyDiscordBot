import discord

token = ""

client = discord.Client(intents=discord.Intents.all())


client.run(token=token)
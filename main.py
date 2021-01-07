# Written by https://github.com/Oleyat/ 
import requests
import discord
import os
import asyncio
import json
import time
import random
import datetime
from operator import itemgetter
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = "bot-token"
  
def get_prefix(bot, message):
  with open ('prefixes.json',  'r') as f:
    prefixes = json.load(f)

  if isinstance(message.channel, discord.channel.DMChannel):
    prefixes = '+'
    return prefixes
  else:
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix= get_prefix)
bot.remove_command("help")

@bot.event
async def on_guild_join(guild):
  with open ('prefixes.json',  'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '+'

  with open ('prefixes.json',  'w') as f:
    json.dump(prefixes, f, indent=4)


extensions = [
  'Commands.stats' ,
  'Commands.help' ,
  'Commands.exchange' ,
]


safeppl = [276035238134808576] #add ur own id or smth, up to you


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name="+help | " + (str(len(bot.guilds))) + " Servers", type=discord.ActivityType.playing,))
    channel = bot.get_channel(723227287918739456)
    await channel.send("Bot is online")

@bot.command()
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await ctx.send(f":ping_pong: Ping: {ping}ms")

#PREFIX CHANGER
@bot.event
async def on_guild_join(guild):
  with open ('prefixes.json',  'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '+'

  with open ('prefixes.json',  'w') as f:
    json.dump(prefixes, f, indent=4)

  channel = bot.get_channel(723267092555497472)
  embed = discord.Embed(color=0x00ff80)
  embed.add_field(name="Guild Status", value="Joined a new guild!", inline=False)
  embed.add_field(name="Guild Amount:", value=(str(len(bot.guilds))), inline=False)
  await channel.send(embed=embed)
@bot.event
async def on_guild_remove(guild):
  with open ('prefixes.json',  'r') as f:
    prefixes = json.load(f)

  prefixes.pop(str(guild.id))

  with open ('prefixes.json',  'w') as f:
    json.dump(prefixes, f, indent=4)
  channel = bot.get_channel(710826168080793630)
  embed = discord.Embed(color=0xff0000)
  embed.add_field(name="Guild Status", value="Left a guild!", inline=False)
  embed.add_field(name="Guild Amount:", value=(str(len(bot.guilds))), inline=False)
  await channel.send(embed=embed)
  
@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
  with open ('prefixes.json',  'r') as f:
    prefixes = json.load(f)
  prefixes[str(ctx.guild.id)] = prefix
  with open ('prefixes.json',  'w') as f:
    json.dump(prefixes, f, indent=4)
  await ctx.send("Prefix has been changed to `" + prefix + "`")

@bot.command()
async def load(ctx, extension):
  if ctx.author.id == 276035238134808576:
    bot.load_extension(f'Commands.{extension}')
    await ctx.send(f'`{extension}` was successfully loaded.')
  else:
    await ctx.send('This command is for the bot developer. You do not have access to use it.')

@bot.command()
async def unload(ctx, extension):
  if ctx.author.id == 276035238134808576:
    bot.unload_extension(f'Commands.{extension}')
    await ctx.send(f'`{extension}` was successfully unloaded.')
  else:
    await ctx.send('This command is for the bot developer. You do not have access to use it.')
@bot.command()
async def reload(ctx, extension):
  if ctx.author.id == 276035238134808576:
    bot.unload_extension(f'Commands.{extension}')
    bot.load_extension(f'Commands.{extension}')
    await ctx.send(f'`{extension}` was successfully reloaded.')
  else:
    await ctx.send('This command is for the bot developer. You do not have access to use it.')

@bot.event
async def on_command_completion(ctx):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    channel = bot.get_channel(697795878626525196)
    embed = discord.Embed(color=0x00ff80)
    embed.add_field(name="User", value=ctx.author, inline=False)
    embed.add_field(name="User Mention", value=ctx.author.mention, inline=False)
    embed.add_field(name="UserID", value=ctx.author.id, inline=False)
    embed.add_field(name="Guild", value='None - Direct Messages', inline=False)
    embed.add_field(name="GuildID", value='None - Direct Messages', inline=False)
    embed.add_field(name="Command", value=ctx.message.content, inline=False)
    await channel.send(embed=embed)
  else:
    channel = bot.get_channel(697795878626525196)
    embed = discord.Embed(color=0x00ff80)
    embed.add_field(name="User", value=ctx.author, inline=False)
    embed.add_field(name="User Mention", value=ctx.author.mention, inline=False)
    embed.add_field(name="UserID", value=ctx.author.id, inline=False)
    embed.add_field(name="Guild", value=ctx.guild, inline=False)
    embed.add_field(name="GuildID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Command", value=ctx.message.content, inline=False)
    await channel.send(embed=embed)




if __name__ == "__main__":
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as error:
      print('{} failed to load.. [{}]'.format(extension, error))
  keep_alive()
  bot.run(TOKEN)

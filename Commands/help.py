import discord
import requests
import datetime, time
from discord.ext import commands
from discord.utils import get

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def help(self, ctx):
      embed=discord.Embed(title='Crypto Statistics Bot', color=0xff6f6f)
      embed.add_field(name="Information", value="""

`Default Prefix: + `
[Invite](https://bit.ly/CryptoStatisticsDCBOT) | [Vote](https://top.gg/bot/723222469086806077/vote) | [Support](https://discord.gg/YjDXEpe)
""", inline=False)
      embed.add_field(name="Commands", value="""

`help` - Sends this message to you.
`ping` - your message -> bot -> discord -> bot -> you
`stats help` - Sends you the latest stats for that currency.
`prefix <new prefix>` - Allows you to change the prefix.


""", inline=False)
      embed.add_field(name="Latest Update", value="""None: `
- None`  """, inline=False)
      embed.set_footer(text="Made with love !")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/723267369732014130/734114655806423150/cryptobot.png")

      await ctx.author.send(embed=embed)
      await ctx.send(":white_check_mark:")

    @help.error
    async def help_handler(self, ctx, error):
      if isinstance(error, commands.CommandInvokeError):
        await ctx.send("""Looks like I can't dm you. Check if you your dms open for server members. To do that simply click:
      
**USER SETTINGS** >>> ** PRIVACY & SAFETY ** >>> **Allow Direct Messages from server members**
      
Once you have enabled it type the command again. You can disable the setting after! """)


def setup(bot):
    bot.add_cog(help(bot))



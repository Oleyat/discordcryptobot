import discord
import requests
import datetime, time
import json
from discord.ext import commands
from discord.utils import get


if __name__ == "__main__":
    main()
    
class exchange(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(aliases=['ee', 'ex'])
    async def exchange(self, ctx, exchange='help'):
      if not exchange or exchange == 'help':
        await ctx.send("""**Command: Stats**
        
        *How to use:*
        
        Type +exchange <exchange name>.

        *Examples*
        
        `+exchange binance`
        `+ex gemini`
        `+ee coinbasepro`
        """)
      else:
        if exchange == 'coinbasepro':
          exchange = (exchange.replace('coinbasepro', 'gdax'))
          print(exchange)

        exxchange = fetch(f'https://api.coincap.io/v2/exchanges/{exchange}')
        exchangeid = exxchange['data']['exchangeId']
        exchangename = exxchange['data']['name']
        exchangerank = exxchange['data']['rank']
        volume = int(float(exxchange['data']['volumeUsd']))
        volformat = (format(volume,','))
        markets = exxchange['data']['tradingPairs']
        exchangelink = exxchange['data']['exchangeUrl']
        embed=discord.Embed(title=f"{exchange}".capitalize() + " - Stats",   url=f"https://coincap.io/exchanges/{exchange}", color=0x4d4d4d)
        embed.add_field(name="ID", value=exchangeid, inline=True)
        embed.add_field(name="Name", value=exchangename, inline=True)
        embed.add_field(name="Rank", value=exchangerank, inline=True)
        embed.add_field(name="Volume(24hr)", value=f'${volformat}', inline=True)
        embed.add_field(name="Markets", value=markets, inline=True)
        embed.add_field(name="Link", value=exchangelink, inline=False)
  

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(exchange(bot))

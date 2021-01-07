import discord
import requests
import datetime, time
import json
from discord.ext import commands
from discord.utils import get


if __name__ == "__main__":
    main()


        
class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(aliases=['crypto', 'ss'])
    async def stats(self, ctx, cryptocurrency='help'):
      if not cryptocurrency or cryptocurrency == 'help':
        await ctx.send("""**Command: Stats**
        
        *How to use:*
        
        Type +stats <crypto>.

        *Examples*
        
        `+stats bitcoin`
        `+crypto bitcoin`
        `+ss bitcoin`
        """)
      else:

        getreqapicrypto = fetch(f'https://api.coincap.io/v2/assets/{cryptocurrency}')
        cryptomaxsupply = getreqapicrypto["data"]['maxSupply']
        if not getreqapicrypto["data"]['maxSupply'] or getreqapicrypto["data"]['maxSupply'] == 'null':
          cryptomaxsupply == 'None'
        else:
          cryptomaxsupply = int(float(getreqapicrypto["data"]['maxSupply']))

        cryptoid =  getreqapicrypto["data"]['id']
        cryptorank = getreqapicrypto["data"]['rank']
        cryptosymbol = getreqapicrypto["data"]['symbol']
        cryptosymbollower = cryptosymbol.lower()
        cryptoname = getreqapicrypto["data"]['name']
        cryptosupply = int(float(getreqapicrypto["data"]['supply']))
        supplyformat = (format(cryptosupply,','))
        cryptomarketcapusd = int(float(getreqapicrypto["data"]['marketCapUsd']))
        cryptomarketcapformat = (format(cryptomarketcapusd,','))
        cryptovol24hour = int(float(getreqapicrypto["data"]['volumeUsd24Hr']))
        cryptovol24hrformat = (format(cryptovol24hour,','))
        cryptopriceusd = int(float(getreqapicrypto["data"]['priceUsd']))
        cryptochangepercent24hr =  int(float(getreqapicrypto["data"]['changePercent24Hr']))
        cryptovwap24hr = int(float(getreqapicrypto["data"]['vwap24Hr']))
        cryptotimestamp = int(float(getreqapicrypto['timestamp']))
        cryptocurrencyz = cryptocurrency
        cryptomaxsupplyformat = (format(cryptomaxsupply,','))



        embed=discord.Embed(title=f"{cryptocurrencyz}".capitalize() + " - Stats",   url=f"https://coincap.io/assets/{cryptocurrencyz}", color=0x4d4d4d)
        embed.add_field(name="ID", value=cryptoid, inline=True)
        embed.add_field(name="Symbol", value=cryptosymbol, inline=True)
        embed.add_field(name="Rank", value=cryptorank, inline=True)
        embed.add_field(name="Price (USD)", value= f"{cryptopriceusd}$", inline=True)
        embed.add_field(name="Market Cap (USD)", value=f"{cryptomarketcapformat}", inline=True)
        embed.add_field(name="Price Change(24hr)", value=f"{cryptochangepercent24hr}%", inline=True)
        embed.add_field(name="Average Price (24hr)", value=f"{cryptovwap24hr}$", inline=True)
        embed.add_field(name="Supply", value= supplyformat, inline=True)
        embed.add_field(name="Max Supply", value= cryptomaxsupplyformat, inline=True)
        embed.add_field(name="Volume USD (24hr)", value= cryptovol24hrformat, inline=True)
        embed.set_thumbnail(url=f"https://cryptoicons.org/api/white/{cryptosymbollower}/400")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(stats(bot))

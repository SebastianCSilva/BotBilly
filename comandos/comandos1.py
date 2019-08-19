import random
import asyncio
import discord
from discord.ext import commands
import aiohttp
import json

class Comandos(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Eventos
    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Game("♂ with his Duck ♂")
        await self.client.change_presence(status=discord.Status.idle, activity=game)
        print("\n Logged in as " + self.client.user.name)

    @commands.command()
    async def hola(self, message):
        await message.send("Hola {0.author.mention}".format(message))

    @commands.command()
    async def PepeHands(self, message):
        await message.send("https://youtu.be/O3L-m7syRyI")

    @commands.command()
    async def gachiclasico(self, message):
        await message.send("https://www.youtube.com/watch?v=JPxfAYYo7NA")

    @commands.command()
    async def gachirandom(self, message):
        lista = ["https://youtu.be/O3L-m7syRyI",
                 "https://www.youtube.com/watch?v=JPxfAYYo7NA",
                 "https://www.youtube.com/watch?v=NdqbI0_0GsM",
                 "https://www.youtube.com/watch?v=ZqrbdXmVr44",
                 "https://www.youtube.com/watch?v=OWNOQA6fWC8",
                 "https://www.youtube.com/watch?v=_o2cr1BP-sk",
                 "https://www.youtube.com/watch?v=tJpjQqpbbY8",
                 "https://www.youtube.com/watch?v=SVHj64ltMb8",
                 "https://www.youtube.com/watch?v=m1_HHVoPjho"]
        await message.send(random.choice(lista))

    @commands.command()
    async def btc(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

        async with aiohttp.ClientSession() as session:  # Async HTTP request

            raw_response = await session.get(url)

            response = await raw_response.text()

            response = json.loads(response)

            await ctx.send("El precio en dolares de Bitcoin es: $" + response['bpi']['USD']['rate'])

    @commands.command()
    async def eth(self, ctx):
        url = 'https://api.cryptonator.com/api/ticker/eth-usd'

        async with aiohttp.ClientSession() as session:  # Async HTTP request

            raw_response = await session.get(url)

            response = await raw_response.text()

            response = json.loads(response)

            await ctx.send("El precio en dolares de Ethereum es: $" + response['ticker']['price'])




def setup(client):
    client.add_cog(Comandos(client))

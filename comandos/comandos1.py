import random
import asyncio
import discord
from discord.ext import commands


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


def setup(client):
    client.add_cog(Comandos(client))

# Work with Python 3.6
import random
import asyncio

import discord
from discord.ext import commands

TOKEN = ''

PREFIX = '♂'
client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    game = discord.Game("♂ with his Duck ♂")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("\n Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


@client.command()
async def hola(message):
    await message.send("Hola {0.author.mention}".format(message))

@client.command()
async def PepeHands(message):
    await message.send("https://youtu.be/O3L-m7syRyI")

@client.command()
async def gachiclasico(message):
    await message.send("https://www.youtube.com/watch?v=JPxfAYYo7NA")
""""
@client.command()
async def help(message):
    await message.send("hola, PepeHands, gachiclasico, gachirandom")
"""

@client.command()
async def gachirandom(message):

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


client.loop.create_task(list_servers())
client.run(TOKEN)
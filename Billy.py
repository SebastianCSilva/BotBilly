# Work with Python 3.6
import random
import asyncio
from discord import Game
from discord.ext.commands import Bot


TOKEN = ''


#client = discord.Client()

PREFIX = '♂'
client = Bot(command_prefix=PREFIX)





@client.command()
async def hola(message):
    await client.say("Hola {0.author.mention}".format(message))


"""
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX+'hola'):
        hola(message)
        #msg = 'Hola {0.author.mention}'.format(message)
        #await client.send_message(message.channel, msg)

"""

@client.command()
async def ClasicGachi():
    await client.say("https://youtu.be/")

@client.command()
async def PepeHands():
    await client.say("'https://youtu.be/O3L-m7syRyI")

@client.command()
async def Cuadrado(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))



"""
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX+'hola'):
        msg = 'Hola {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
"""

""" Code nuevo  """


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="♂ with his Duck ♂"))
    print("\n Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
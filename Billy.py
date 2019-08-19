# Work with Python 3.7
import random
import asyncio
import os
import discord
from discord.ext import commands

TOKEN = ''

PREFIX = ['♂','.']
client = commands.Bot(command_prefix=PREFIX)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'comandos.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'comandos.{extension}')

@client.command()
async def reload(ctx, extension):
    client.load_extension(f'comandos.{extension}')
    client.unload_extension(f'comandos.{extension}')

for filename in os.listdir('./comandos'):
    if filename.endswith('.py'):
        client.load_extension(f'comandos.{filename[:-3]}')


client.run(TOKEN)
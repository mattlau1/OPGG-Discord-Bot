'''
jdaobot for Discord

Written in Python 3.8.5 64-bit

Usage: python3 bot.py

Features:
    - League of Legends champion build [Usage: /build [lane] [champion]]
        - uses http://lol.lukegreen.xyz/ api to scrape opgg data
        - sends top 5 builds for champion in specified lane
'''

import discord
import re
from random import randint
import requests
import json
import urllib.request
from secret.secret_token import token_class
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def build(ctx, *args):
    '''
    Build Command
    Lists builds for champion from op.gg

    Usage: /build [lane] [champion]
    '''
    print(f'Build cmd detected')
    await ctx.send("hi")
    if len(args) != 2:
        await ctx.send(f'Usage: /build [lane] [champion]')
    else:
        build_url = f'http://lol.lukegreen.xyz/build/{args[0]}/{args[1]}'
        build = ''
        if requests.get(build_url).status_code != 500:
            await ctx.send(f'Lane: {args[0]}')
            await ctx.send(f'Champ: {args[1]}')
            
            with urllib.request.urlopen(build_url) as url:
                data = json.loads(url.read().decode())
                for num in range(1, 6):
                    build += f'Build {num}: '
                    for item in data[f'build_{num}']:
                        build += (item.lstrip("(\"\'")) + ', '
                    build += '\n'

            await ctx.send(build)
        else:
            await ctx.send(f'Check Spelling u idiot')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    print("help command triggered")
    embed=discord.Embed(title="Commands", color=0x0f7ef5)
    embed.set_thumbnail(url="https://i.ibb.co/sHC7w0d/Screenshot-1.jpg")
    embed.add_field(
        name="/build [ top | mid | jg | adc | sup ] [champion]",
        value="Sends Top 5 Builds for Champion in specified lane"
    )
    await ctx.send(embed=embed)

bot.run(token_class().get_token())    

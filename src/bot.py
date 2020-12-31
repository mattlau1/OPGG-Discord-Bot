'''
Kevin Nguyen Bot for Discord

Written in Python 3.8.5 64-bit

Usage: python3 bot.py

Features:
    - League of Legends champion build [Usage: /build [lane] [champion]]
        - uses http://lol.lukegreen.xyz/ api to scrape opgg data
        - sends top 5 builds for champion in specified lane
'''

import json
import urllib.request
import re
import io
import discord
import requests
from discord.ext import commands
from runes import get_runes
from secret.secret_token import token_class

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    '''
    Prints to owner in console when bot is ready.
    '''
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(aliases=['build'])
async def build_cmd(ctx, *args):
    '''
    Build Command
    Lists builds for champion from op.gg

    Usage: /build [lane] [champion]
    '''
    print('Build cmd detected')
    if len(args) != 2:
        await ctx.send('Usage: /build [lane] [champion]')
    else:
        build_url = f'http://lol.lukegreen.xyz/build/{args[0]}/{args[1]}'
        build = ''
        if requests.get(build_url).status_code != 500:
            await ctx.send(f'Lane: {args[0].capitalize()}')
            await ctx.send(f'Champ: {args[1].capitalize()}')

            # get items
            with urllib.request.urlopen(build_url) as url:
                data = json.loads(url.read().decode())
                for num in range(1, 6):
                    build += f'Build {num}: '
                    for item in data[f'build_{num}']:
                        build += (item.lstrip("(\"\'")) + ', '
                    build += '\n'
                    build = re.sub(r'(,)[\s]$', '', build)
            await ctx.send(build)

            # send runes
            with io.BytesIO() as image_binary:
                get_runes(args[1], args[0]).save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary, filename='runes.png'))

        else:
            await ctx.send('Check Spelling u idiot')

bot.remove_command('help')
@bot.command(aliases=['help'])
async def help_cmd(ctx):
    '''
    Sends all commands to user
    '''
    print("help command triggered")
    embed = discord.Embed(
        title="Commands",
        url="https://github.com/mattlau1/Kevin-Nguyen-Bot", color=0x0f7ef5
    )
    embed.set_thumbnail(url="https://i.ibb.co/sHC7w0d/Screenshot-1.jpg")
    embed.add_field(
        name="/build [ top | mid | jg | adc | sup ] [champion]",
        value="Sends Top 5 Builds for Champion in specified lane"
    )
    await ctx.send(embed=embed)

bot.run(token_class().get_token())

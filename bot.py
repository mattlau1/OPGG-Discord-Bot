'''
jdaobot for Discord

Written in Python 3.8.5 64-bit

Usage: python3 bot.py

Features:
    - jdaomode on [Usage: /jdaomode]
        - changes avatar to jdao1's avatar
        - changes nickname to jdao1
        - sends random jdao1 quote on every message
        - sends "hi ____" if "i'm ____" is detected
    - jdaomode off [Usage: /jdaomode]
        - changes avatar to Kevin Nguyen
        - changes nickname to Kevin Nguyen
        - sends "kys echau" on every message [ITS A JOKE]
    - League of Legends champion build
        - uses http://lol.lukegreen.xyz/ api to scrape opgg data

    WIP:
        - /build [lane] [champion]
        - Storing jdaomode in pickle file
'''

import discord
import re
from random import randint
import requests
import json
import urllib.request
from secret.secret_token import token_class


TOKEN = token_class().get_token()

jono_quotes = [
    'ded lmao', 'lmao', 'ya', 'ayy lmao', 'whoopsie', 'bruh', 'bruh', 'bruh',
    'leg?', 'woooow', 'reeaallyy?', 'no way', 'wai u lai'
]
client = discord.Client()
jdaomode = True

def get_pfp(user):
    '''
    returns a profile picture based on given user
    '''
    # "avatars/kevin.png"
    dir1 = "avatars/kevin.png"
    dir2 = "avatars/jdao.png"
    if user == 'kevin':
        fp = open(dir1, 'rb')
        return fp.read()
    else:
        fp = open(dir2, 'rb')
        return fp.read()

@client.event
async def on_message(message):
    global jdaomode
    channel = message.channel
    
    if message.author == client.user:
        return

    if message.content.startswith('/build'):
        '''
        Build Command
        Lists builds for champion from op.gg

        Usage: /build [lane] [champion]
        '''
        msg = message.content.split(' ')
        if len(msg) < 3:
            await channel.send(f'Usage: /build [lane] [champion]')
        else:
            await channel.send(f'lane: {msg[1]}')
            await channel.send(f'champ: {msg[2]}')
            
            build_url = f'http://lol.lukegreen.xyz/build/{msg[1]}/{msg[2]}'
            build = ''
            with urllib.request.urlopen(build_url) as url:
                data = json.loads(url.read().decode())
                for num in range(1, 6):
                    build += f'Build {num}: '
                    for item in data[f'build_{num}']:
                        build += (item.lstrip("(\"\'")) + ', '
                    
                    build += '\n'

            await channel.send(build)

    elif message.content.startswith('/jdaomode'):
        if jdaomode == True:
            jdaomode = False
            await channel.send('JDAOMODE DEACTIVATED')
            await message.guild.get_member(client.user.id).edit(nick='Kevin Nguyen')
            await client.user.edit(password=None, avatar=get_pfp('kevin'))
        else:
            jdaomode = True 
            await channel.send('JDAOMODE ACTIVATED')
            await message.guild.get_member(client.user.id).edit(nick='jdao1')
            await client.user.edit(password=None, avatar=get_pfp('jdao'))

    elif message.content.startswith('im ') and jdaomode == True:
        regex = re.sub('(im )', 'hi ', message.content, 1, flags=re.I)
        await channel.send(regex)

    elif jdaomode == True:
        rand = randint(0, len(jono_quotes) - 1)
        await channel.send(jono_quotes[rand])

    elif re.match('.*', message.content):
        await channel.send('kys echau')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

client.run(TOKEN)
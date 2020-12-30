'''
jdaobot for Discord

Written in Python 3.8.5 64-bit

Usage: python3 bot.py

Features:
    - jdaomode on [Usage: /jdaomode]
        - changes avatar to jdao1's avatar
        - changes nickname to jdao1
        - sends random jdao1 quote on every message
        - sends "hi ____" if "im ____" is detected
    - jdaomode off [Usage: /jdaomode]
        - changes avatar to Kevin Nguyen
        - changes nickname to Kevin Nguyen
        - stops spamming
    - League of Legends champion build [Usage: /build [lane] [champion]]
        - uses http://lol.lukegreen.xyz/ api to scrape opgg data
        - sends top 5 builds for champion in specified lane

    WIP:
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
jdaomode = False


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(TOKEN)

class command():
    def __init__(self, message):
        self.message = message
        self.channel = message.channel

    async def build_cmd(self):
        '''
        Build Command
        Lists builds for champion from op.gg

        Usage: /build [lane] [champion]
        '''
        print(f'Build cmd detected, self.message{self.message}')
        msg = self.message.content.split(' ')
        if len(msg) < 3:
            await self.channel.send(f'Usage: /build [lane] [champion]')
        else:
            build_url = f'http://lol.lukegreen.xyz/build/{msg[1]}/{msg[2]}'
            build = ''
            if requests.get(build_url).status_code != 500:
                await self.channel.send(f'Lane: {msg[1]}')
                await self.channel.send(f'Champ: {msg[2]}')
                
                with urllib.request.urlopen(build_url) as url:
                    data = json.loads(url.read().decode())
                    for num in range(1, 6):
                        build += f'Build {num}: '
                        for item in data[f'build_{num}']:
                            build += (item.lstrip("(\"\'")) + ', '
                        build += '\n'

                await self.channel.send(build)
            else:
                await self.channel.send(f'Check Spelling u idiot')
        
    async def jdaomode_cmd(self, jdaomode):
        '''
        Jdaomode Command

        - jdaomode on 
            - changes avatar to jdao1's avatar
            - changes nickname to jdao1
            - sends random jdao1 quote on every message
            - sends ``"hi ____"`` if ``"i'm ____"`` is detected
        - jdaomode off 
            - changes avatar to Kevin Nguyen
            - changes nickname to Kevin Nguyen
            - stops spamming

        Usage: /jdaomode
        '''
        if jdaomode == True:
            jdaomode = False
            await self.channel.send('JDAOMODE DEACTIVATED')
            await self.message.guild.get_member(client.user.id).edit(nick='Kevin Nguyen')
            await client.user.edit(password=None, avatar=get_pfp('kevin'))
        else:
            jdaomode = True 
            await self.channel.send('JDAOMODE ACTIVATED')
            await self.message.guild.get_member(client.user.id).edit(nick='jdao1')
            await client.user.edit(password=None, avatar=get_pfp('jdao'))

    async def help_cmd(self):
        await self.channel.send('''
        Features:
        - jdaomode on ``[Usage: /jdaomode]``
            - changes avatar to jdao1's avatar
            - changes nickname to jdao1
            - sends random jdao1 quote on every message
            - sends ``"hi ____"`` if ``"i'm ____"`` is detected
        - jdaomode off ``[Usage: /jdaomode]``
            - changes avatar to Kevin Nguyen
            - changes nickname to Kevin Nguyen
            - stops spamming
        - League of Legends champion build ``[Usage: /build [lane] [champion]]``
            - sends top 5 builds for champion in specified lane
        ''')

    async def im_cmd(self):
        regex = re.sub('(im )', 'hi ', self.message.content, 1, flags=re.I)
        await self.channel.send(regex)

    async def quote_cmd(self):
        rand = randint(0, len(jono_quotes) - 1)
        await self.channel.send(jono_quotes[rand])

@client.event
async def on_message(message):
    global jdaomode
    cmds = command(message)
    
    if message.author == client.user:
        return

    if message.content.startswith('/build'):
        cmds.build_cmd()

    elif message.content.startswith('/jdaomode'):
        cmds.jdaomode_cmd(jdaomode)

    elif message.content.startswith('/help'):
        cmds.help_cmd()

    elif message.content.startswith('im ') and jdaomode == True:
        cmds.im_cmd()

    elif jdaomode == True:
        cmds.quote_cmd()

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



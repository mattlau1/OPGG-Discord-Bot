'''
jdaobot for Discord

Written in Python 3.8.5 64-bit

Features:
    - jdaomode on [Usage: !jdaomode]
        - changes avatar to jdao1's avatar
        - changes nickname to jdao1
        - sends random jdao1 quote on every message
        - sends "hi ____" if "i'm ____" is detected
    - jdaomode off [Usage: !jdaomode]
        - changes avatar to Kevin Nguyen
        - changes nickname to Kevin Nguyen
        - sends "kys echau" on every message [ITS A JOKE]
    
    WIP:
        - !opgg [name]
'''
import discord
import re
from random import randint
from scrapeGG import scrapeGG
from secret_token import token_class

token = token_class()
TOKEN = token.get_token()

jono_quotes = [
    'ded lmao', 'lmao', 'ya', 'ayy lmao', 'whoopsie', 'bruh', 'bruh', 'bruh',
    'leg?', 'woooow', 'reeaallyy?', 'no way', 'wai u lai'
]
client = discord.Client()
jdaomode = True

# load profile pics
pfp1_path = "avatars/kevin.png"
fp1 = open(pfp1_path, 'rb')
pfp1 = fp1.read()

pfp2_path = "avatars/jdao.png"
fp2 = open(pfp2_path, 'rb')
pfp2 = fp2.read()

@client.event
async def on_message(message):
    global jdaomode
    channel = message.channel
    
    if message.author == client.user:
        return

    if message.content.startswith('!opgg'):
        summoner = message.content.split(' ')
        if len(summoner) < 2:
            await channel.send(f'Usage: !opgg [name]')
        else:
            await channel.send(f'{summoner[1]}')

        

    elif message.content.startswith('!jdaomode'):
        if jdaomode == True:
            jdaomode = False
            await channel.send('JDAOMODE DEACTIVATED')
            await message.guild.get_member(client.user.id).edit(nick='Kevin Nguyen')
            await client.user.edit(password=None, avatar=pfp1)
        elif jdaomode == False:
            jdaomode = True 
            await channel.send('JDAOMODE ACTIVATED')
            await message.guild.get_member(client.user.id).edit(nick='jdao1')
            await client.user.edit(password=None, avatar=pfp2)

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
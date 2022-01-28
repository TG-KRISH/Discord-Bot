import discord
import logging
import random 
from colorama import init
from termcolor import colored
import json
import math
import datetime
import time
import choice
import os
import requests
from asyncio import sleep
from keep_alive import keep_alive
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import ActivityType


def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)
 

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('.help'))


@client.event
async def on_guild_join(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)
 
      prefixes[str(guild.id)] = '.'

      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open ('prefixes.json', 'w') as f:
                   json.dump(prefixes, f, indent=4)
@client.event
async def on_guild_remove(guild):
  print (f'G0_B0T has been removed from guild |"{guild}"|, |"{guild.id}"')

@client.event
async def on_guild_join(guild):
  print (f'G0_B0T has been added to the guild "{guild}"')

@client.command()
async def changeprefix(ctx, prefix):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix


      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

      await ctx.send(f'Prefix changed to: {prefix}')
      await ctx.message.add_reaction('❗')

@client.command()
async def K(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.add_reaction('❗')
    await ctx.send (f'Kicked {member.mention}')


@client.command()
async def B(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.add_reaction('❗')
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def U(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.add_reaction('❗')
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('❗')
        await ctx.send('Invaild command used, type **.help** for command sheet!')


@client.command()
async def cls(ctx, amount=1000000000000000000001):
    await ctx.message.add_reaction('❗')
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send(f'Pong! {round (client.latency *100)}ms')

@client.command(aliases=['8ball', 'test'])
async def ai (ctx, *, question):
 responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
'abnegation'
'not now',
'ban',
'choice',
'cold shoulder',
'declension',
'declination',
'defiance',
'disallowance',
'disapproval',
'disavowal',
'disclaimer',
'discountenancing',
'disfavor',
'dissent',
'enjoinment',
'exclusion',
'forbidding',
'interdiction',
'knockback',
'negation',
"it would not happen",
'nix',
'no',
'nonacceptance',
'noncompliance',
'nonconsent',
'option',
"pass",
'prohibition',
'proscription',
'rebuff',
'refutation',
'regrets',
'rejection',
'renouncement',
'renunciation',
'repudiation',
'reversal',
'thumbs down',
'turndown',
'veto',
'withholding',
'writ',
"hmm....! yes!",
"I SAY NO!",
"well.. i say yes",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful.",
"affirmative.",
'amen',
'fine',
'good',
'okay',
'true',
'yeah',
'all right',
'beyond a doubt',
'by all means',
'certainly',
'definitely',
'even so',
'exactly',
'gladly',
'good enough', 
'granted',
'indubitably',
'just so',
'most assuredly',
'naturally',
'of course',
'positively',
'precisely',
'sure thing',
'surely',
'undoubtedly',
'unquestionably',
'very well',
'willingly',
'without fail',
'yep']
 

 await ctx.message.add_reaction('❗')
 await ctx.send(f'Command: {question}\nAnswer: {random.choice(responses)}')

tell = ['Hey..',"whats'up", 'hola!','hello','Hi!','bonjour','buenas noches','buenos dias','good day','greetings','hey']
@client.command()
async def hi(ctx):
  await ctx.message.add_reaction('❗')
  await ctx.send(f'{random.choice(tell)}' + f' {ctx.message.author.name}')

@client.command()
async def how_to(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('for discord bot ask the user MrGokulBig#9503')
    await ctx.send(
        'you just ask and tell, what name do you want for your bot')

@client.command()
async def whatsmyname(ctx):
 await ctx.send(f"Your name is {ctx.message.author.name}")
  

@client.command(pass_content=True)
async def echo(ctx,*, msg):
  await ctx.message.add_reaction('❗')
  await ctx.send(msg)

@client.command()
async def spam(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send(f'Warning, {ctx.message.author.name}')
    await sleep(5)
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')     
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**') 



keep_alive()

TOKEN = 'Ur Token Here'

client.run(TOKEN)

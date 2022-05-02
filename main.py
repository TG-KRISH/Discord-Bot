import discord
import random 
import datetime
from urllib import parse, request
import re
import choice
import termcolor
import colorama
import os
import requests
from asyncio import sleep
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import has_permissions




client = commands.Bot(command_prefix = '.')
                

@client.event
async def on_member_join(ctx, member: discord.Member,guild):
  await ctx.send(f'{member.mention} has joined {guild}')

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Streaming(name=".help", url="https://www.twitch.tv/mrgokulbig_27"))


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10000001):
  await ctx.channel.purge(limit=amount)
  await ctx.message.add_reaction('⚡')
  await ctx.send(f'Cleared messges.')


@client.event
async def on_guild_remove(guild):
  print (f'Speed_B0T has been removed from guild |"{guild}"|, |"{guild.id}"')

@client.event
async def on_guild_join(guild):
  print (f'Speed_B0T has been added to the guild "{guild}"')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.add_reaction('⚡')
    await ctx.send (f'Kicked {member.mention}')


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Banned {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.add_reaction('⚡')
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('⚡')
        await ctx.send(f'Invaild command , type `.help` for command sheet!')

@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('⚡')
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
'refutation',
'regrets',
'rejection',
'renouncement',
'renunciation',
'repudiation',
'reversal',
'thumbs down',
'turndown',
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
'yep'
"Yes"
"No"
"Yes, if Tacorilla wills it"
"No... I mean yes... Well... Ask again later"
"The answer is unclear... Seriously I double checked"
"I won't answer that, but Zcotticus will"
"It's a coin flip really..."
"Yes, he will... Sorry I wan't really listening"
"I could tell you but I'd have to permanently ban you"
"Yes, No, Maybe... I don't know, could you repeat the question?"
"If you think I'm answering that, you're clearly mistaking me for Xanbot."
"Do you REALLY want me to answer that? OK... Maybe "
"YesNoYesNoYesNoYesNoYesNo "
"Ask yourself this question in the mirror three times, the answer will become clear "
"You want an answer? OK, here's your answer: "
 ]
 

 await ctx.message.add_reaction('⚡')
 await ctx.send(f"mmm..... thinking for the question '{question}'")
 await sleep(5)
 await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

tell = ['Hey..',"whats'up", 'hola!','hello','Hi!','bonjour','buenas noches','buenos dias','good day','greetings','hey']
@client.command()
async def hi(ctx):
  await ctx.message.add_reaction('⚡')
  await ctx.send(f'{random.choice(tell)}' + f' {ctx.message.author.mention}')


@client.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Speed_B0T", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
     embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@client.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
     print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])



@client.listen()
async def on_message(message):
    if "Code" in message.content.lower():
        await message.channel.send('This is the code of the bot https://github.com/TG-KRISH/Discord-Bot')
        await client.process_commands(message)


@client.command()
async def how_to(ctx):
    await ctx.message.add_reaction('⚡')
    await ctx.send('for discord bot ask the user @MrGokulBig#9503')
    await ctx.send(
        'you just ask and tell, what name do you want for your bot')

@client.command()
async def whatsmyname(ctx):
 await ctx.send(f"Your name is {ctx.message.author.mention}")
  
G0 = ['My name is Speed. I am Speed and Reliable.','Hello!, I am Speed','i am Speed and made by MrGokulBig#9503']

@client.command()
async def name(ctx):
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'{random.choice(G0)}')

@client.command(pass_content=True)
async def echo(ctx,*, msg):
  await ctx.message.add_reaction('⚡')
  await ctx.send(msg)


@client.command()
async def spam(ctx):
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Warning, {ctx.message.author.mention}')
    await sleep(5)
    await ctx.send('Y/N')
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



client.run("")

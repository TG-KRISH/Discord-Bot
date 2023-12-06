import discord
import random 
import datetime
import youtube_dl
import json
import re
import termcolor
import colorama
import os
import requests
import asyncio
from asyncio import sleep
from keep_alive import keep_alive
from discord.ext import commands
from discord.errors import Forbidden
from urllib import parse, request
from discord.ext.commands import has_permissions
import functools
import itertools
import math

client = commands.Bot(command_prefix=commands.when_mentioned_or('$','.','>','?','!'), help_command=None)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Streaming(name=".help", url="https://www.twitch.tv/mrgokulbig_27"))

@client.command(aliases=['h','commands'])
async def help(ctx, args=None):
    help_embed = discord.Embed(title="Commands!", color=discord.Color.random())
    command_names_list = [x.name for x in client.commands]

    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(client.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `.help <command name>` for more details about each command.",
            inline=False
        )
    
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=client.get_command(args).help
        )

    else:
        help_embed.add_field(
            name="No commands found",
            value="sorry dude!"
        )
    await ctx.send(embed=help_embed)
    await ctx.message.add_reaction('⚡')

@client.command()
@commands.has_permissions(administrator=True)
async def audit(ctx):
    guild = ctx.guild
    entries = guild.audit_logs(limit=100)
    await ctx.send(f'Audit Log: {entries}')

@client.command()
async def embed(ctx):
  user = ctx.author
  perms = ctx.author.permissions_in(ctx.channel)
  if perms.administrator:
    em = discord.Embed(description='What would you like the title to be?', color = discord.Colour.random())
    await user.send(embed=em)
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    title = msg.content
    em = discord.Embed(description='What would you like the Description to be?', color = discord.Colour.red())
    await user.send(embed=em)
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    desc = msg.content
    em = discord.Embed(title = "**Confirm Channel**", description = "Choose a channel for this msg to be in. Put Channel ID", color = discord.Colour.red())
    await user.send(embed=em)
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    channel = msg.content
    em = discord.Embed(title=title, description=desc,color=discord.Colour.red())
    await ctx.channel.send(embed=em)
    await ctx.message.add_reaction('⚡')
    return 


@client.event
async def on_member_join(ctx, member: discord.Member,guild):
  await ctx.send(f'{member.mention} has joined {guild}')




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10000001):
  await ctx.channel.purge(limit=amount)
  await ctx.message.add_reaction('⚡')
  await ctx.send(f'Cleared messges.')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{user.mention} has been banned!')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.add_reaction('⚡')
    await ctx.send (f'Kicked {member.mention}')




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

@client.command()
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
"If you think I'm answering that, you're clearly mistaking me for Xanclient."
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
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, duration: int = None):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")

    if not mute_role:
        # If the role doesn't exist, create it
        mute_role = await ctx.guild.create_role(name="Muted", reason="To mute members")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)

    await member.add_roles(mute_role, reason=f"Muted by {ctx.author}")
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'{member.mention} has been muted.')

    if duration:
        await asyncio.sleep(duration)
        await member.remove_roles(mute_role, reason=f"Automatic unmute after {duration} seconds")
        await ctx.send(f'{member.mention} has been automatically unmuted after {duration} seconds.')


@client.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
    await ctx.message.add_reaction('⚡')

@client.command()
async def serverinfo(ctx):
    await ctx.message.add_reaction('⚡')
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Speed_B0T", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
  
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)


@client.command(aliases=['userinfo','information'])
async def myinfo(message):
        emb14 = discord.Embed(
            title=f"@{message.author} info:",
            colour=discord.Colour.dark_blue()
        )
        emb14.set_image(url=message.author.avatar_url)
        emb14.add_field(name=f"Name", value=f"{message.author}", inline=True)
        emb14.add_field(name=f"Discord Joined date", value=f"{message.author.created_at}", inline=True)
        emb14.add_field(name=f"Server Joined date", value=f"{message.author.joined_at}", inline=True)
        await message.channel.send(embed=emb14)
        await ctx.message.add_reaction('⚡')

  
G0 = ['My name is Speed. I am Speed and Reliable.','Hello!, I am Speed','i am Speed and made by MrGokulBig#9503']


@client.command()
async def name(ctx):
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'{random.choice(G0)}')

@client.command()
async def youtube(ctx, *, query):
    query = parse.urlencode({'search_query': query})
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'YouTube Search: https://www.youtube.com/results?{query}')

@client.command()
async def google(ctx, *, query):
    query = parse.urlencode({'q': query})
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Google Search: https://www.google.com/search?{query}')

@client.command()
async def roll(ctx, sides: int = 6, num_of_dice: int = 1):
    rolls = [random.randint(1, sides) for _ in range(num_of_dice)]
    total = sum(rolls)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Rolling {num_of_dice} {sides}-sided dice: {rolls}\nTotal: {total}')

@client.command()
async def flip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Flipping a coin... It\'s {result}!')

@client.command()
async def compliment(ctx):
    compliments = ["You're amazing!", "You're one in a million!", "You bring joy to others!", "You're incredibly talented!"]
    await ctx.message.add_reaction('⚡')
    await ctx.send(random.choice(compliments))

@client.command()
async def insult(ctx):
    insults = ["You're as useful as a screen door on a submarine.", "Your IQ is lower than room temperature.", "You're a living example of why some animals eat their young."]
    await ctx.message.add_reaction('⚡')
    await ctx.send(random.choice(insults))

@client.command()
async def servericon(ctx):
    server = ctx.guild
    icon_url = server.icon_url
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'This is the server icon: {icon_url}')

@client.command()
async def poll(ctx, *options):
    if len(options) < 2 or len(options) > 10:
        await ctx.send("Please provide 2 to 10 options for the poll.")
        return

    formatted_options = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(options)])
    poll_message = await ctx.send(f"**Poll:**\n{formatted_options}")

    for i in range(len(options)):
        await poll_message.add_reaction(f"{i + 1}\u20e3")  # Emoji numbers

    await ctx.message.add_reaction('⚡')

@client.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'The current time is {current_time}.')

@client.command()
async def nickname(ctx, member: discord.Member, new_nickname):
    await member.edit(nick=new_nickname)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Changed {member.mention}\'s nickname to {new_nickname}.')

@client.command()
async def membercount(ctx):
    member_count = ctx.guild.member_count
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'The server currently has {member_count} members.')

@client.command()
async def quote(ctx, *, message_id: int):
    try:
        quoted_message = await ctx.channel.fetch_message(message_id)
        await ctx.message.add_reaction('⚡')
        await ctx.send(f'Quoting message from {quoted_message.author.mention}:\n"{quoted_message.content}"')
    except discord.NotFound:
        await ctx.send(f"Message with ID {message_id} not found.")

@client.command()
async def emojilist(ctx):
    emoji_list = [str(emoji) for emoji in ctx.guild.emojis]
    emojis = " ".join(emoji_list)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Emojis in this server: {emojis}')

@client.command()
async def reverse(ctx, *, text):
    reversed_text = text[::-1]
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Reversed text: {reversed_text}')

@client.command()
async def choose(ctx, *choices):
    if not choices:
        await ctx.send("Please provide choices to choose from.")
        return

    chosen = random.choice(choices)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'I choose: {chosen}')

@client.command()
async def wanted(ctx, *, user: discord.Member):
    wanted_text = f"**WANTED!**\n\n{name} is wanted for various crimes against the server.\n\nReward: 1000 Discord Coins"
    await ctx.message.add_reaction('⚡')
    await ctx.send(wanted_text)

@client.command()
async def dumbrate(ctx, *, user: discord.Member = None):
    user = user or ctx.author
    dumbness = random.randint(1, 100)

    await ctx.message.add_reaction('⚡')
    await ctx.send(f"{user.mention}'s dumbness level is {dumbness}/100. 🤔")


@client.command()
async def calculate(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.message.add_reaction('⚡')
        await ctx.send(f'Result: {result}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

import math

@client.command()
async def sqrt(ctx, number: float):
    if number < 0:
        await ctx.send("Cannot calculate the square root of a negative number.")
        return

    result = math.sqrt(number)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Square root of {number} is {result}')

@client.command()
async def factorial(ctx, number: int):
    if number < 0:
        await ctx.send("Factorial is not defined for negative numbers.")
        return

    result = math.factorial(number)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'The factorial of {number} is {result}')

@client.command()
async def randomnum(ctx, start: int, end: int):
    if start > end:
        await ctx.send("Please provide valid range (start should be less than or equal to end).")
        return

    random_number = random.randint(start, end)
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Random number between {start} and {end}: {random_number}')

@client.command()
async def percentage(ctx, part: float, whole: float):
    if whole == 0:
        await ctx.send("Cannot calculate percentage when the denominator is zero.")
        return

    percentage_value = (part / whole) * 100
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'{part} is {percentage_value:.2f}% of {whole}')

riddles = [
  "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
  "The more you take, the more you leave behind. What am I?",
  "I'm tall when I'm young, and short when I'm old. What am I?",
  "The person who makes it, sells it. The person who buys it never uses it. What is it?",
  "What has keys but can't open locks?"
]

@client.command()
async def riddle(ctx):
  random_riddle = random.choice(riddles)
  await ctx.message.add_reaction('⚡')
  await ctx.send(f'Here\'s a riddle for you:\n"{random_riddle}"')

@client.command()
async def answer(ctx, *, guess):
    correct_answers = ["echo", "footsteps", "candle", "coffin", "piano"]

    if guess.lower() in correct_answers:
        await ctx.message.add_reaction('⚡')
        await ctx.send(f'Congratulations! "{guess}" is the correct answer.')
    else:
        await ctx.send(f'Sorry, "{guess}" is not the correct answer. Keep trying!')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Joined {channel}')

@client.command()
async def leave(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        await voice_channel.disconnect()
        await ctx.message.add_reaction('⚡')
        await ctx.send(f'Left the voice channel.')
    else:
        await ctx.send('Not currently in a voice channel.')

@client.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()

    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_channel.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Now playing: {url}')

@client.command()
async def stop(ctx):
    voice_channel = ctx.voice_client
    if voice_channel.is_playing():
        voice_channel.stop()
        await ctx.message.add_reaction('⚡')
        await ctx.send('Stopped the music.')
    else:
        await ctx.send('No music is currently playing.')

@client.command()
async def pause(ctx):
    voice_channel = ctx.voice_client
    if voice_channel.is_playing():
        voice_channel.pause()
        await ctx.message.add_reaction('⚡')
        await ctx.send('Paused the music.')
    else:
        await ctx.send('No music is currently playing.')

@client.command()
async def resume(ctx):
    voice_channel = ctx.voice_client
    if voice_channel.is_paused():
        voice_channel.resume()
        await ctx.message.add_reaction('⚡')
        await ctx.send('Resumed the music.')
    else:
        await ctx.send('Music is not currently paused.')


@client.command()
async def joke(ctx):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    setup = joke_data["setup"]
    punchline = joke_data["punchline"]
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'**Joke:**\n{setup}\n*{punchline}*')

@client.command()
async def rng(ctx, min_val: int, max_val: int):
    await ctx.message.add_reaction('⚡')
    await ctx.send(f'Random Number: {random.randint(min_val, max_val)}')


@client.command(pass_content=True)
async def echo(ctx,*, msg):
  await ctx.message.add_reaction('⚡')
  await ctx.send(msg)

@client.command()
async def spam(ctx):
    user = ctx.author
    await ctx.message.add_reaction('⚡')
    await ctx.send('check ur DM!!')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')
    await user.send('**SPAMING**')

keep_alive()
   
client.run("Your Bot token......")

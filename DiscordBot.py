import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

'''
@bot.command(name='1', help='Responds with a random quote')
async def bot_msg(ctx):
    dumb_quotes = ['Unfortunately that pride is overshadowed by all this unyielding rage',
                   'I am perfect and you will quote everything I say',
                   'Gonna need a senzu for that one']

    respond_msg = random.choice(dumb_quotes)
    await ctx.channel.send(respond_msg)

bot.run(TOKEN)
'''


def input_shi(message):
    dumb_quotes = ['Unfortunately that pride is overshadowed by all this unyielding rage',
                   'I am perfect and you will quote everything I say',
                   'Gonna need a senzu for that one']

    respond_msg = random.choice(dumb_quotes)
    return respond_msg


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected to the following guild:'
          f'{guild.name}(id:{guild.id})'
          )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the jungle'
    )


@client.event
async def on_message(message):
    print(type(message.content))
    if message.author == client.user:
        return
    respond_msg = "You're rude, shut up"
    #respond_msg = input_shi(message)
    await message.channel.send(respond_msg)
    if message.content == 'exep':
        raise discord.DiscordException


@client.event
async def error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled error: {args[0]}\n')
        else:
            raise
 

client.run(TOKEN)


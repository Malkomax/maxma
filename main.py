'''This is the main runner code for the SipsVs bot.'''
import os

import discord
from dotenv import load_dotenv

working_directory = os.getcwd()
add_to_env = os.path.join(working_directory, '.env')
load_dotenv(add_to_env)

client = discord.Client()


@client.event
async def on_ready():
    '''On first event, set up client'''
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    '''Describes behavior on message receive'''
    if message.author == client.user:
        return

    if message.content.startswith('>_> hello'):
        # print(f'Message received from {message.author}!')
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))

import discord
import os
from dotenv import load_dotenv

'''
This is a slightly hacky way to get the environment token to load correctly
If I don't do this step, the token won't show up.
'''
working_directory = os.getcwd()
add_to_env = os.path.join(working_directory, '.env')
load_dotenv(add_to_env)

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>_> hello'):
        # print(f'Message received from {message.author}!')
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
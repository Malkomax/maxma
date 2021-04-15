#! /home/ubuntu/sips-vs/sipsenv/bin/python3
'''This is admin-level controls for main runner code for the SipsVs bot.'''
import os

import discord
from dotenv import load_dotenv


def env_setup():
    '''Adds the .env variables so that tokens work'''
    working_directory = os.getcwd()
    add_to_env = os.path.join(working_directory, '.env')
    load_dotenv(add_to_env)


if __name__ == "__main__":
    client = discord.Client()

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name='sipsvs. respectfully.'))
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        '''Describes behavior on message receive'''
        if message.author == client.user:
            return
        else:
            roles = message.author.roles
            for role in roles:
                if role.id == 701965615866576937:
                    if message.content.startswith('sipsvs admin'):
                        await message.channel.send('admin command recognized')
            return

    env_setup()
    client.run(os.getenv('TOKEN'))

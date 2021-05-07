#! /home/ubuntu/sips-vs/sipsenv/bin/python3
'''This is the main runner code for the SipsVs bot.'''
import os
import re

import discord
from dotenv import load_dotenv

import command_runner


def env_setup():
    '''Adds the .env variables so that tokens work'''
    working_directory = os.getcwd()
    add_to_env = os.path.join(working_directory, '.env')
    load_dotenv(add_to_env)


if __name__ == "__main__":
    client = discord.Client()

    daBabySpaceBlocker = re.compile('da[\\w\\s]+baby', re.IGNORECASE)
    daBabyNoSpaceBlocker = re.compile('dababy', flags=re.IGNORECASE)

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name='sipsvs in dev'))
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        daBabyDenier = [daBabyNoSpaceBlocker.search(message.content),
                        daBabySpaceBlocker.search(message.content)]
        # print(daBabyDenier)
        '''Describes behavior on message receive'''
        if message.author == client.user:
            return
        if message.content.startswith('sipsvs'):
            arg = str.strip(message.content[len('sipsvs'):])
            is_admin = False  # Removed admin check to disable sipsvs admin
            # admin_check = message.author.roles
            # for role in admin_check:
            #     if role.id == 701965615866576937:
            #         is_admin = True
            if arg.startswith('admin') and is_admin:
                await message.channel.send('admin input recognized')
            else:
                result = await command_runner.command_processor(arg)
                await message.channel.send(result)
        elif 'respectfully' in message.content:
            await message.add_reaction('🕶')
        elif daBabyDenier[0] is not None or daBabyDenier[1] is not None:
            await message.add_reaction('👎🏽')

    env_setup()
    client.run(os.getenv('TOKEN'))

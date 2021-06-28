#! /home/ubuntu/sips-vs/sipsenv/bin/python3
'''This is the main runner code for the SipsVs bot.'''
import asyncio
import os
import random
import re

import discord
# from discord_slash import SlashCommand
from dotenv import load_dotenv

import admin_controls
import command_runner

guild_ids = ['698755318792060929']


def env_setup():
    '''Adds the .env variables so that tokens work'''
    working_directory = os.getcwd()
    add_to_env = os.path.join(working_directory, '.env')
    load_dotenv(add_to_env)


if __name__ == "__main__":
    client = discord.Client()
    # client = discord.Client(intents=discord.Intents.all())
    # slash = SlashCommand(client, sync_commands=True)

    daBRe = 'd(|\\))(\\s+)?[ax@4]([\\w\\s]+)?b(\\s+)?[ax@4](\\s+)?b(\\s+)?y'
    # d (any whitespace) a/x/@/4 (whitespace/character) -? b a b y
    # (same whitespace stuff, not sure why (|\\) is present)

    # daBabyRegex; flake8 complained

    daBabyBlocker = re.compile(daBRe, re.IGNORECASE)

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name='sipsvs, less respectfully'))
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        daBabyDenier = daBabyBlocker.search(message.content)
        '''Describes behavior on message receive'''
        if message.author == client.user:
            return
        if message.content.startswith('sipsvs'):
            arg = str.strip(message.content[len('sipsvs'):])
            is_admin = False  # Removed admin check to disable sipsvs admin
            admin_check = message.author.roles
            for role in admin_check:
                if role.id == 701965615866576937:
                    is_admin = True
            if arg.startswith('admin') and is_admin:
                await message.reply('admin input recognized')
                target = arg[len('admin '):]
                result = admin_controls.command_processor(target)
            else:
                result = await command_runner.command_processor(arg)
                await message.reply(result)
        elif 'respectfully' in message.content:
            delay = random.randint(1, 19)
            await asyncio.sleep(delay)
            # await message.reply('respectfully.')
            await message.add_reaction('🕶')
        elif daBabyDenier is not None:
            await message.add_reaction('👎🏽')

    env_setup()
    client.run(os.getenv('TOKEN'))

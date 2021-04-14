#! /home/ubuntu/sips-vs/sipsenv/bin/python3
'''This is the main runner code for the SipsVs bot.'''
import os
import random
import asyncio

import discord
from dotenv import load_dotenv


def env_setup():
    '''Adds the .env variables so that tokens work'''
    working_directory = os.getcwd()
    add_to_env = os.path.join(working_directory, '.env')
    load_dotenv(add_to_env)


async def respectfully(arg: str) -> str:
    '''adds respect. respectfully.'''
    await asyncio.sleep(10)
    return f'{arg}. respectfully.'


async def hap_birt(arg: str) -> str:
    '''
    Sends a happy birthday message!
    '''
    return f'HAPPY BDAY, {arg}'


async def combat(combatant_one: str, combatant_two: str) -> str:
    '''
    This function takes both combatants and rolls dice for them both.
    '''
    print(combatant_one, combatant_two)
    c1_roll = random.randint(1, 20)
    c2_roll = random.randint(1, 20)
    roll_string = f'{combatant_one} rolled a {c1_roll}, while {combatant_two} rolled a {c2_roll}!'
    if c2_roll > c1_roll:  # c2 wins
        result = f'{combatant_one} has been vanquished by {combatant_two}.'
    elif c1_roll > c2_roll:  # c1 wins
        result = f'{combatant_one} has ANNIHILATED {combatant_two}!'
    else:  # Tie
        result = 'Alas, it was a stalemate. Neither could best the other.'
    return f'{roll_string} {result}'


async def command_processor(argument: str) -> str:
    '''
    This function determines the behavior of the sipsvs bot after the sipsvs keyword.
    '''
    if len(argument) == 0 or argument == 'help':
        return str('Hey, thanks for asking for help!\n\n' +
        'To make it clear your homies hate someone, use ```css\nsipsvs fuck [name]```\n' +
        'To shame someone, use ```css\nsipsvs shame [name]```\n' +
        'To cause a pvp battle, use ```css\nsipsvs pvp [combatant one] vs [combatant two]```\n' +
        'To generate a battle against sips, use ```css\nsipsvs [opponent]```\n' +
        'To wish a friend a birthday, use ```css\nsipsvs hbd [name]```\n' +
        'To provide additional respect, use ```css\nsipsvs respectfully [text]```\n')
    if argument.startswith('shame'):
        arg = str.strip(argument[len('shame'):])
        return f'SHAME UPON {arg}'
    if argument.startswith('fuck'):
        arg = str.strip(argument[len('fuck'):])
        return f'fuck {arg} all my homies hate {arg}'
    if argument.startswith('pvp'):
        arg = str.strip(argument[len('pvp'):])
        combatants = arg.split(' vs ')
        return await combat(str.strip(combatants[0]), str.strip(combatants[1]))
    if argument.startswith('hbd'):
        arg = str.strip(argument[len('hbd'):])
        return await hap_birt(arg)
    if argument.startswith('respectfully'):
        arg = str.strip(argument[len('respectfully'):])
        return await respectfully(arg)
    return await combat('sips', argument)


if __name__ == "__main__":
    client = discord.Client()

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name='sipsvs & Malcolm!'))
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        '''Describes behavior on message receive'''
        if message.author == client.user:
            return
        if message.content.startswith('sipsvs'):
            arg = str.strip(message.content[len('sipsvs'):])
            result = await command_processor(arg)
            await message.channel.send(result)

    env_setup()
    client.run(os.getenv('TOKEN'))

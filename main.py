#! /usr/bin/python3
'''This is the main runner code for the SipsVs bot.'''
import os
import random

import discord
from dotenv import load_dotenv

def env_setup():
    '''Adds the .env variables so that tokens work'''
    working_directory = os.getcwd()
    add_to_env = os.path.join(working_directory, '.env')
    load_dotenv(add_to_env)

def combat(combatant_one:str, combatant_two:str) -> str:
    '''
    This function takes both combatants and rolls dice for them both.
    '''
    print(combatant_one, combatant_two)
    c1_roll = random.randint(1, 20)
    c2_roll = random.randint(1, 20)
    roll_string = f'{combatant_one} rolled a {c1_roll}, while {combatant_two} rolled a {c2_roll}!'
    if c2_roll > c1_roll: #c2 wins
        result = f'{combatant_one} has been vanquished by {combatant_two}.'
    elif c1_roll > c2_roll: #c1 wins
        result = f'{combatant_one} has ANNIHILATED {combatant_two}!'
    else: # Tie
        result = 'Alas, it was a stalemate. Neither could best the other.'
    return f'{roll_string} {result}'

def command_processor(argument:str) -> str:
    '''
    This function determines the behavior of the sipsvs bot after the sipsvs keyword.
    '''
    if len(argument) == 0 or argument == 'help':
        return str('Hey, thanks for asking for help!\n\n' +
        'To make it clear your homies hate someone, use ```css\nsipsvs fuck [name]```\n' +
        'To shame someone, use ```css\nsipsvs shame [name]```\n' +
        'To cause a pvp battle, use ```css\nsipsvs pvp [combatant one] vs [combatant two]```\n' +
        'To generate a battle against sips, use ```css\nsipsvs [opponent]```')
    if argument.startswith('shame'):
        arg = str.strip(argument[len('shame'):])
        return f'SHAME UPON {arg}'
    if argument.startswith('fuck'):
        arg = str.strip(argument[len('fuck'):])
        return f'fuck {arg} all my homies hate {arg}'
    if argument.startswith('pvp'):
        arg = str.strip(argument[len('pvp'):])
        combatants = arg.split(' vs ')
        return combat(str.strip(combatants[0]), str.strip(combatants[1]))
    # No other option here
    fight = combat('sips', argument)
    return fight

if __name__ == "__main__":
    client = discord.Client()

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name='the command sipsvs'))
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        '''Describes behavior on message receive'''
        if message.author == client.user:
            return
        if message.content.startswith('sipsvs'):
            arg = str.strip(message.content[len('sipsvs'):])
            await message.channel.send(command_processor(arg))

    env_setup()
    client.run(os.getenv('TOKEN'))

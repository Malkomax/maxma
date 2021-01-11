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

def combat(opponent:str) -> str:
    '''
    This function takes the opponent's name and computes dice rolls for both Sips and the opponent.
    '''
    sips_roll = random.randint(1, 20)
    opponent_roll = random.randint(1, 20)
    roll_string = f'Sips rolled a {sips_roll}, while {opponent} rolled a {opponent_roll}!'
    if opponent_roll > sips_roll: #Opponent wins
        result = f'Sips has been vanquished by {opponent}.'
    elif sips_roll > opponent_roll: #Sips wins
        result = f'Sips has ANNIHILATED {opponent}!'
    else: # Tie
        result = f'Alas, it was a stalemate. Neither Sips nor {opponent} could best the other.'
    return f'{roll_string} {result}'

def command_processor(argument:str) -> str:
    if len(argument) == 0 or argument == 'help':
        return 'Hey, thanks for asking for help!\nTo make it clear your homies hate someone, use ```css\nsipsvs fuck [name]```\nTo shame someone, use ```css\nsipsvs shame [name]```\nTo generate a battle, use ```css\nsipsvs [opponent]```'
    if argument.startswith('shame'):
        arg = str.strip(argument[len('shame'):])
        return f'SHAME UPON {arg}'
    elif argument.startswith('fuck'):
        arg = str.strip(argument[len('fuck'):])
        return f'fuck {arg} all my homies hate {arg}'
    else:
        fight = combat(argument)
        return fight

if __name__ == "__main__":
    client = discord.Client()

    @client.event
    async def on_ready():
        '''On first event, set up client'''
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='the command sipsvs'))
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

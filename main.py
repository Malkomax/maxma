#! ./sipsenv/bin/python
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

if __name__ == "__main__":
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
        if message.content.startswith('sipsvs'):
            arg = str.strip(message.content[len('sipsvs'):])
            if len(arg) == 0 or arg == 'help':
                await message.channel.send('Hey, thanks for asking for help! \n' +
                'Use ```css\nsipsvs [opponent]\n``` to generate a battle!')
            else:
                opponent = str.strip(message.content[len('sipsvs'):])
                fight = combat(opponent)
                await message.channel.send(fight)

    env_setup()
    client.run(os.getenv('TOKEN'))

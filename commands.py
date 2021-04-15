import random
import asyncio


async def shame(argument: str) -> str:
    '''Used for shaming'''
    arg = str.strip(argument[len('shame'):])
    return f'SHAME upon {arg}!'


async def fuck(argument: str) -> str:
    arg = str.strip(argument[len('fuck'):])
    return f'fuck {arg} all my homies hate {arg}'


async def respectfully(argument: str) -> str:
    '''adds respect. respectfully.'''
    arg = str.strip(argument[len('respectfully'):])
    await asyncio.sleep(3)
    return f'{arg}. respectfully.'


async def hap_birt(argument: str) -> str:
    '''
    Sends a happy birthday message!
    '''
    arg = str.strip(argument[len('hbd'):])
    return f'HAPPY BDAY, {arg}'


async def combat(combatant_one: str, combatant_two: str) -> str:
    '''
    This function takes both combatants and rolls dice for them both.
    '''
    print(combatant_one, combatant_two)
    c1_roll = random.randint(1, 20)
    c2_roll = random.randint(1, 20)
    roll_string = (f'{combatant_one} rolled a ' +
                   f'{c1_roll}, while {combatant_two} rolled a {c2_roll}!')
    if c2_roll > c1_roll:  # c2 wins
        result = f'{combatant_one} has been vanquished by {combatant_two}.'
    elif c1_roll > c2_roll:  # c1 wins
        result = f'{combatant_one} has ANNIHILATED {combatant_two}!'
    else:  # Tie
        result = 'Alas, it was a stalemate. Neither could best the other.'
    return f'{roll_string} {result}'

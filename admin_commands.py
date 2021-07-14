import random
import asyncio


async def bonk(argument: str) -> str:
    '''bonk'''
    arg = str.strip(argument[len('bonk'):])
    delay = random(300, 900)
    await asyncio.sleep(delay)
    return f'*bonks {arg}*'

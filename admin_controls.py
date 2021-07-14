import admin_commands as commands


async def command_processor(argument: str) -> str:
    '''
    This function determines
    the behavior of the sipsvs bot after the sipsvs keyword.
    '''
    if len(argument) == 0 or argument == 'help':
        return str('this is the admin input menu.')
    if argument.startswith('bonk'):
        return await commands.bonk(argument)
    return f'Unrecognized admin command {argument}'
    # return str('Hey, thanks for asking for help!\n\n' +
    #            'To make it clear your homies hate someone, use ' +
    #            '```css\nsipsvs fuck [name]```\n' +
    #            'To shame someone, use ' +
    #            '```css\nsipsvs shame [name]```\n' +
    #            'To cause a pvp battle, use ' +
    #            '```css\nsipsvs pvp [combatant one] ' +
    #            'vs [combatant two]```\n' +
    #            'To generate a battle against sips, use ' +
    #            '```css\nsipsvs [opponent]```\n' +
    #            'To wish a friend a birthday, use ' +
    #            '```css\nsipsvs hbd [name]```\n' +
    #            'To provide additional respect, use ' +
    #            '```css\nsipsvs respectfully [text]```\n')

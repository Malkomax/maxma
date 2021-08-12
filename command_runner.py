import commands


async def command_processor(argument: str) -> str:
    '''
    This function determines
    the behavior of the sipsvs bot after the sipsvs keyword.
    '''
    if len(argument) == 0 or argument == 'help':
        return str('Hey, thanks for asking for help!\n\n' +
                   'To make it clear your homies hate someone, use ' +
                   '```css\nsipsvs fuck [name]```\n' +
                   'To shame someone, use ' +
                   '```css\nsipsvs shame [name]```\n' +
                   'To cause a pvp battle, use ' +
                   '```css\nsipsvs pvp [combatant one] ' +
                   'vs [combatant two]```\n' +
                   'To generate a battle against sips, use ' +
                   '```css\nsipsvs [opponent]```\n' +
                   'To wish a friend a birthday, use ' +
                   '```css\nsipsvs hbd [name]```\n' +
                   'To provide additional respect, use ' +
                   '```css\nsipsvs respectfully [text]```\n')  # +
#                #    'To encode or decode David\'s Cipher, use' +
#                #    '```css\nsipsvs ddec [ciphertext]```\n' +
#                #    'To encode or decode David\'s Cipher, use' +
#                #    '```css\nsipsvs denc [ciphertext]```\n')
    if argument.startswith('shame'):
        return await commands.shame(argument)
    if argument.startswith('cancel'):
        return await commands.cancel(argument)
    if argument.startswith('fuck'):
        return await commands.fuck(argument)
    if argument.startswith('pvp'):
        arg = str.strip(argument[len('pvp'):])
        if 'vs' not in arg:
            return ('Invalid syntax. Please try again, using\n' +
                    '```css\nsipsvs pvp [combatant one] ' +
                    'vs [combatant two]```\n')
        combatants = arg.split(' vs ')
        return await commands.combat(str.strip(combatants[0]),
                                     str.strip(combatants[1]))
    if argument.startswith('hbd'):
        return await commands.hap_birt(argument)
    if argument.startswith('respectfully'):
        return await commands.respectfully(argument)
    return await commands.combat('sips', argument)

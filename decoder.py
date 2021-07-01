FWD = {
    '-': 'a', ',': '_c/x_', ':': 'd', '3': 'e', ';': 'f', ')': '_g/y_',
    '$': '_h/j_', '8': 'i', '@': '_k/l_', '&': 'k', '"': 'l', "'": 'm',
    '!': '_b/n_', '9': 'o', '0': 'p', '1': 'q', '4': 'r', '/': 's',
    '5': 't', '7': 'u', '?': 'v', '2': 'w', '6': 'y', '.': 'z', ' ': ' '
}

REV = {
    'a': '-', 'b': '!', 'c': ',', 'd': ':', 'e': '3', 'f': ';',
    'g': ')', 'h': '$', 'i': '8', 'j': '$', 'k': '@', 'l': '@',
    'm': "'", 'n': '!', 'o': '9', 'p': '0', 'q': '1', 'r': '4',
    's': '/', 't': '5', 'u': '7', 'v': '?', 'w': '2', 'x': ',',
    'y': '6', 'z': '.', ' ': ' '
}


async def encode(in_string: str) -> str:
    out = ''
    for s in in_string:
        out += REV[s]
    return out


async def decode(in_string: str) -> str:
    out = ''
    for s in in_string:
        out += FWD[s]
    return out

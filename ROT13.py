"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    alphabets_sm = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_bg = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    for char in message:
        if char.isupper() and char in alphabets_bg:
            res.append(alphabets_bg[(alphabets_bg.find(char) + 13) % len(alphabets_bg)])
        elif not char.isupper() and char in alphabets_sm:
            res.append(alphabets_sm[(alphabets_sm.find(char) + 13) % len(alphabets_sm)])
        else:
            res.append(char)
    return ''.join(res)

# -------------------------------------------------------------
# @ Author: Phillip Flores
# @ Cypher Encoding
# My implementation generates a random key & xors it with each
# character of the string. The result is encoded. To reverse it
# the xor is called again with the key.
# ------------------------------------------------------------

import random
global key
key = random.choice([str(char) for char in range(10)])


def xor_encode(string):
    return ''.join([str(chr(ord(string[char]) ^ ord(key))) for char in range(len(string))])


if __name__ == '__main__':
    s = 'hello world!'
    encode = xor_encode(s)
    decode = xor_encode(encode)
    print(f' input: {s}')
    print(f'encode: {encode}')
    print(f'decode: {decode}')


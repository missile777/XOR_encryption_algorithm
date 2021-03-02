# -------------------------------------------------------------
# @ Author: Phillip Flores
# @ Cypher Encoding
# @ My implementation generates a random key at the function
# @ call. The key is simple to hack with an injection. The
# @ function returns an encoded output of the input string.
# ------------------------------------------------------------


def xor_encode(string):
    import random
    key = random.choice([str(char) for char in range(10)])
    return ''.join([str(chr(ord(string[char]) ^ ord(key))) for char in range(len(string))])


print(xor_encode('cypher!'))


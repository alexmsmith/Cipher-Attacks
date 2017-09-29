#python cipher.py e key.txt plaintext.txt 
#python cipher.py d key.txt ciphertext.txt 

def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S # return

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def streamcipher(key):
    S = KSA(key)
    #print(S)
    return PRGA(S)


if __name__ == '__main__':
    import sys

    file = open(sys.argv[2], 'r')
    key = file.read()
    file.close()

    file = open(sys.argv[3], 'r')
    if sys.argv[1] == 'e':  #encryption
        plaintext = file.read()
    else:                   #decryption
        ciphertext = file.read()
    file.close()


    def convert(s):
        return [ord(c) for c in s]

    key = convert(key)
    keystream = streamcipher(key)

    if sys.argv[1] == 'e':  #encryption
        for c in plaintext:
            sys.stdout.write("%02X" % (ord(c) ^ next(keystream)))
    else:                   #decryption
        n = 0
        while n < len(ciphertext):
            x = int(ciphertext[n:n+2], 16)
            sys.stdout.write( chr(x ^ next(keystream)) )
            n += 2

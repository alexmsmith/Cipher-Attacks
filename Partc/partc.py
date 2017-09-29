# HOW TO USE
# 1) To Test, Encrypt Both PlainTextFileA and PlainTextFileB With The Same Key
    # And Store In Relative CipherTextFile 'A' And 'B'
# 2) Enter: 'partc.py ciphertextfileA.txt ciphertextfileB.txt plaintextfileA.txt' Into Console
# 3) This Will Print The Decrypted Message To Console Of ciphertextfileB

if __name__ == '__main__':
    import sys

    #Read cipherfileA into system
    cipherfileA = open(sys.argv[1], 'r')
    ciphertextfileA = cipherfileA.read()
    cipherfileA.close()

    #Read cipherfileB into system
    cipherfileB = open(sys.argv[2], 'r')
    ciphertextfileB = cipherfileB.read()
    cipherfileB.close()

    #Read plainfileA into system
    plainfileA = open(sys.argv[3], 'r')
    plaintextfileA = plainfileA.read()
    plainfileA.close()

    #Here I've converted the string 'plaintextfileA' to a hexadecimal value
    pT = ""
    for c in plaintextfileA:
            b = "%02X" % (ord(c))
            pT+=str(b)
    
    #XOR both ciphertextfileA and plaintextfileA to extract the key
    n=0
    message = ""
    while n < len(ciphertextfileA):
        #Go through each hexValue in ciphertextfileA
        hexValueC = int(ciphertextfileA[n:n+2], 16)
        #Go through each hexValue in the plaintextfileA
        hexValueP = int(pT[n:n+2], 16)
        #XOR both hexValueC and hexValueP
        xORed = (hexValueC ^ hexValueP)

        #Need to convert value of XORed to a hexadecimal value
        xORH = hex(xORed)[2:]
        #Go through each hexValue in ciphertextfileB
        x = int(ciphertextfileB[n:n+2], 16)
        #Go through each hexValue in xORH(xorHex)
        y = int(xORH, 16)
        #XOR both y and x
        value = (x ^ y)
        #Append each value to the message string
        message+=str((chr(value)))
        n+=2
#Print the decrypted message
print("Decrypted Message: %s." % message)

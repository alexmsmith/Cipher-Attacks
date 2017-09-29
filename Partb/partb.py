# HOW TO USE
# 1) Enter: 'partb.py ciphertext.txt 10 15 100GBP **Enter Amount Here**' - Into Console
# 2) Store The Output Of 'Modified' Into 'test.txt' File Provided In Directory
# 3) Enter: 'cipher.py d key.txt test.txt' - Into Console
# 4) This Will Print The Modified String To Console

if __name__ == '__main__':
    import sys

    #Load the ciphertext file and store in variable 'ciphertext'
    cipherfile = open(sys.argv[1], 'r')
    ciphertext = cipherfile.read()
    cipherfile.close();

    #Position 10
    k1 = sys.argv[2]
    k1Int = int(k1)-1
    #Position 15
    k2 = sys.argv[3]
    k2Int = int(k2)
    original = sys.argv[4]    #Original plaintext (100GBP)
    replacement = sys.argv[5] #Replacement plaintext
    selectedCipher = ciphertext[k1Int*2:k2Int*2] #Select sub-string of ciphertext between K1 and K2

    #Convert original 100GBP to hexadecimal value
    originalHex = ""
    for c in original:
        oH = "%02X" % (ord(c))
        originalHex+=str(oH)

    #Convert replacement to hexadecimal value
    replacementHex = ""
    for c in replacement:
        rE = "%02X" % (ord(c))
        replacementHex+=str(rE)
    
    #XOR Orginal with selectedCipher, producing the key
    n=0
    key = ""

    while n < len(selectedCipher):
        #Go through each hexValue in selectedCipher
        hexValueC = int(selectedCipher[n:n+2], 16)
        #Go through each hexValue in the originalHex
        hexValueP = int(originalHex[n:n+2], 16)
        #XOR both hexValueC and hexValueP
        xORed = (hexValueC ^ hexValueP)
        #Convert back into a hexadecimal value and store each in 'kE'
        kE = "%02X" % xORed
        #Append to key string
        key+=str(kE)
        #Move onto the next hexadecimal value
        n+=2

    #XOR hexValueR(replacementHex) and hexValueK(key)
    m=0
    encryptedReplacement = ""

    while m < len(replacementHex):
        hexValueR = int(replacementHex[m:m+2], 16)
        hexValueK = int(key[m:m+2], 16)

        XOR = (hexValueR ^ hexValueK)
        #convert back into a hexadecimal value and store each in 'xH'
        xH = "%02X" % XOR
        #Append to encryptedReplacement string 
        encryptedReplacement+=str(xH)
        #Move onto the next hexadecimal value
        m+=2
    
    Mod = ciphertext.replace(selectedCipher, encryptedReplacement)
    print("Ciphertext: "+ciphertext)
    print("Modified:   "+Mod)
#cipher.py e/d key.txt plaintext.txt/ ciphertext.txt
# HOW TO USE
# 1) Enter: 'parta.py ciphertext.txt'
# 2) Wait Until The Brute-Force Attack Is Complete
# 3) This Will Print The Plaintext And Key Along With The Time It Took To Finish The Attack

import time #Used to calculate how long it would take for the program to finish
import re #RegularExpression functionality for plaintext detection
keyList = [] #This array will store all possible keys that are found within the keyspace
startLoop = 97 #Decimal value for 'a'
endLoop = 123 #Decimal value for 'z'

start_time = time.time() #Execute start time

def KSA(key):
	keylength = len(key)

	S = list(range(256))

	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % keylength]) % 256
		S[i], S[j] = S[j], S[i]

	return S

def PRGA(S):
	i = 0
	j = 0
	while True:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]

		K = S[(S[i] + S[j]) % 256]
		yield K

#Each key in the keyList array will be passed into the streamcipher function
def streamcipher(key):
	S = KSA(key)
	return PRGA(S)
	
if __name__ == '__main__':
	import sys

	cipherFile = open(sys.argv[1], 'r') #Open the cipherFile that is read from the console
	ciphertext = cipherFile.read() #Read this file and store in ciphertext
	cipherFile.close() #This file is no longer needed, and it can be close

	#Each loop represents each character within the keysize, total of 6
	#To increase/decrease the size of the key, we can uncomment/comment related code
	for c1 in range(startLoop, endLoop):
		for c2 in range(startLoop, endLoop):
			for c3 in range(startLoop, endLoop):
				for c4 in range(startLoop, endLoop):
					#for c5 in range(startLoop, endLoop):
						#for c6 in range(startLoop, endLoop):
							initialList = [c1, c2, c3, c4] #c5, #c6]
							
							#Convert each decimal to a character
							char1 = chr(c1)
							char2 = chr(c2)
							char3 = chr(c3)
							char4 = chr(c4)
							#char5 = chr(c5)
							#char6 = chr(c6)
	
							#Create new array and append the characters
							charList = [char1, char2, char3, char4] #char5, #char6]

							#The charList array is then converted to a string (key)
							key = ''.join(str(e) for e in charList) #strList
							#We then append the key to the keyList array
							keyList.append(key)

					#c6 = c6 + 1
				#c5 = c5 + 1
			c4 = c4 + 1
		c3 = c3 + 1
	c2 = c2 + 1

	#The convert function will separate each key into individual characters 
	def convert(s):
		return [ord(c) for c in s]

	for key in keyList:
		key = convert(key)
		keystream = streamcipher(key) #The key processed through the keystream
		n = 0
		sString = ""
		while n < len(ciphertext):
			x = int(ciphertext[n:n+2], 16)
			character = chr(x ^ next(keystream)) #XOR the first bits of both ciphertext and keystream
			string = ''.join(character)
			sString+=str(string)
			n += 2
		if re.match("^[A-Za-z0-9 -]*$", sString): #If anything but unspecified symbols are found..
		#Print the key and also the plaintext message
			KEY=""
			for k in key:
				keyC = chr(k)
				KEY+=str(keyC)
			print("Key: "+KEY)
			print("String: "+sString)
			break #break loop
print("---%s seconds ---" % (time.time() - start_time)) #Print total execution time to console
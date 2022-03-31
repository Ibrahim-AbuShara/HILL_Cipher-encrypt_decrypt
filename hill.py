# Python3 code to implement Hill Cipher
import numpy as np
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keyMatrix = [[0] * 3 for i in range(3)]

invkeyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]


# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

#tirm the string and add xxxx to %3
def tirming(string):
	m=[]#for tirming the mwssage
	
 
	while(len(string)%3!=0):
		string+='x'
	while(string):
		m.append(string[:3])
		string=string[3:]
	return m

#GCD
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
# Inverse
def modinv(a):
    gcd, x, y = egcd(a,26)
    if gcd != 1:
         raise Exception("Sorry,modular inverse does not exist")  # modular inverse does not exist
    else:
        return x % 26

# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = alpha.index(key[k])
			k += 1
#get inverce matrix key for decryption
def get_invkey(keyMatrix):
    npkey=np.array(keyMatrix)
    det = round((np.linalg.det(npkey)))
    det_inv=modinv(det%26)
    inv_matrix=(det*np.linalg.inv(keyMatrix))
    
    invkeyMatrix=inv_matrix*det_inv
    invkeyMatrix=invkeyMatrix%26
    return (invkeyMatrix)


		
    
    
# Following function encrypts the message
def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

#return the incroted vector as alphats
def HillCipher(message, key):

	# Get key matrix from the key string
	getKeyMatrix(key)

	# Generate vector for the message
	
	for i in range(3):
		messageVector[i][0] = alpha.index(message[i])

	
	# the encrypted vector
	encrypt(messageVector)

	# Generate the encrypted text
	CipherText = []
	for i in range(3):
		CipherText.append(alpha[cipherMatrix[i][0]])
	
	# Finally get the ciphertext
	return (CipherText)
#decrypt
def decrypt(c, key):
	getKeyMatrix(key)
	invkeyMatrix=get_invkey(keyMatrix)
	for i in range(3):
		cipherMatrix[i][0] = alpha.index(c[i])
		
	npcipher=np.array(cipherMatrix)
	message_matrix=np.dot(invkeyMatrix,npcipher).round()
	message_matrix=message_matrix%26
	message_matrix=message_matrix.tolist()
	msg=[]
	for i in range(3):
		msg.append(alpha[int(message_matrix[i][0])])
	return(msg)

def start_encryption(key,message):
		c=[]#for append the encrypted message
		message=tirming(message)
	#encrypt
		for i in range(len(message)):
			c.append(HillCipher(message[i], key))
		c=[''.join(x) for x in c]
		cypher = ' '.join([str(elem) for elem in c]).replace(' ','')
		return cypher

def start_decryption(key,cypher):
	i=0
	p=[]#for append the dncrypted message
	cypher=tirming(cypher)
	for i in range(len(cypher)):
		p.append(decrypt(cypher[i],key))
	p=[''.join(x) for x in p]
	plain = ' '.join([str(elem) for elem in p]).replace(' ','')
	return plain

    
# Driver Code
# def main():
# 	key = 'ciphering'.lower()
# 	message = 'safemessages'.lower()
# 	cypher=start_encryption(key,message)
# 	print('Cypher-Text: ',cypher)
# 	pt=start_decryption(key,cypher)
# 	print('Plain-Text: ',pt)
	

# if __name__ == "__main__":
# 	main()



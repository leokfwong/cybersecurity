import string
import math
import re
import shift_cipher

# Create dictionary for alphabet and indices
alphabet = string.ascii_uppercase
index = list(range(len(alphabet)))
dict_alphabet = dict(zip(alphabet, index))
dict_index = dict(zip(index, alphabet))
ENG_PROBABILITY = 0.065

class vigenereCipher:
	"""
	Object containing methods to encrypt and decrypt a Vigenere cipher given a message and a key.
	"""
	# Encrypt message given a key
	def encrypt(self, plaintext, key):
		plaintext = plaintext.upper()
		text = ""
		offset = 0
		for i in range(len(plaintext)):
			if plaintext[i].isalpha():
				text += dict_index[(dict_alphabet[plaintext[i]] + dict_alphabet[key[(i - offset) % len(key)]]) % len(dict_alphabet)]
			else:
				text += plaintext[i]
				offset += 1
		return text

	# Decrypt cipher given a key
	def decrypt(self, cipher, key):
		cipher = cipher.upper()
		text = ""
		offset = 0
		for i in range(len(cipher)):
			if cipher[i].isalpha():
				text += dict_index[(dict_alphabet[cipher[i]] - dict_alphabet[key[(i - offset) % len(key)]]) % len(dict_alphabet)]
			else:
				text += cipher[i]
				offset += 1
		return text

	# Find the length of the unknown key
	def findKeyLength(self, cipher, verbose=False):
		cipher = re.sub(r"[^A-Z]+", "", cipher.upper())
		sum_array = []
		# Iterate through potential key lengths
		for i in range(1, int(len(cipher) / 50)):
			current = [cipher[index] for index, value in enumerate(cipher) if index % i == 0]
			current_text = "".join(current)
			sc = shift_cipher.shiftCipher()
			broken = sc.break_shift(current_text)
			if i <= len(cipher) / 2:
				sum_array.append(broken["sum"])
			if verbose:
				print(f"Key of length {i}, sum={broken['sum']}")
		# Fetch top closest potential lengths
		diff_array = [abs(x - ENG_PROBABILITY) for x in sum_array]
		top = sorted(range(len(diff_array)), key=lambda k: diff_array[k])[:5]
		top = [x + 1 for x in top]
		min_length = min(top)
		if verbose:
			print(f"Potential key length is {min_length}")
		return min_length

	# Break Vigenere cipher
	def breakVigenere(self, cipher, key_length, verbose=False):
		cipher = re.sub(r"[^A-Z]+", "", cipher.upper())
		broken_key = ""
		for i in range(key_length):
			current = [value for index, value in enumerate(cipher) if index % (key_length) == i]
			current_text = "".join(current)
			sc = shift_cipher.shiftCipher()
			broken = sc.break_shift(current_text, verbose=False)
			broken_key += dict_index[broken["k"]]
			if verbose:
				print(f"Iteration {i}, k={broken['k']}, ({dict_index[broken['k']]})")
		if verbose:
			print(f"The key is {broken_key}")
		return broken_key

# Helper function to read and process text into a string
def readTxtString(path):
	with open(path, "r") as f:
		plaintext = f.read().replace("\n", "")
		plaintext = re.sub(r'\s+', ' ', plaintext)
		return plaintext

# Create vigenere object
vig = vigenereCipher()
		
'''
To encrypt or decrypt messages given a key
'''
# Load plaintext and set key
plaintext = readTxtString("plaintext/test.txt")
key = "MAMBA"
# Encrypt plaintext
encrypted_message = vig.encrypt(plaintext, key)
print(f"The encrypted message is {encrypted_message}")
# Decrypt cipher
decrypted_message = vig.decrypt(encrypted_message, key)
print(f"The decrypted message is {decrypted_message}")

'''
To break an encrypted text without a key
'''
# Load cipher with unknown key
cipher = readTxtString("cipher/cipher.txt")
# Break Vigenere cipher
key_length = vig.findKeyLength(cipher, verbose=True)
broken_key = vig.breakVigenere(cipher, key_length, verbose=True)
broken_cipher = vig.decrypt(cipher, broken_key)
# Write to file
with open("cipher/broken_key.txt", "w") as text_file:
    text_file.write(broken_key)
with open("cipher/broken_cipher.txt", "w") as text_file:
    text_file.write(broken_cipher)

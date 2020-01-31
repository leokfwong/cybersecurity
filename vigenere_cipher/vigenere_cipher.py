import string
import math

# Create dictionary for alphabet and indices
alphabet = string.ascii_uppercase
index = list(range(len(alphabet)))
dict_alphabet = dict(zip(alphabet, index))
dict_index = dict(zip(index, alphabet))

class vigenereCipher:
	"""
	Object containing methods to encrypt and decrypt a Vigenere cipher given a message and a key.
	"""
	# Encrypt message given a key
	def encrypt(self, plaintext, key):
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
		text = ""
		offset = 0
		for i in range(len(cipher)):
			if cipher[i].isalpha():
				text += dict_index[(dict_alphabet[cipher[i]] - dict_alphabet[key[(i - offset) % len(key)]]) % len(dict_alphabet)]
			else:
				text += cipher[i]
				offset += 1
		return text

# Plaintext and key
plaintext = "DO YOU KNOW THE LAND WHERE THE ORANGE TREE BLOSSOMS? THE COUNTRY OF GOLDEN FRUITS AND MARVELOUS ROSES, WHERE THE BREEZE IS SOFTER AND BIRDS LIGHTER,WHERE BEES GATHER POLLEN IN EVERY SEASON, AND WHERE SHINES AND SMILES, LIKE A GIFT FROM GOD, AN ETERNAL SPRINGTIME UNDER AN EVER-BLUE SKY! ALAS! BUT I CANNOT FOLLOW YOU TO THAT HAPPY SHORE FROM WHICH FATE HAS EXILED ME! THERE! IT IS THERE THAT I SHOULD LIKE TO LIVE, TO LOVE, TO LOVE, AND TO DIE! IT IS THERE THAT I SHOULD LIKE TO LIVE, IT IS THERE, YES, THERE!"
key = "AMBROISETHOMAS"

# Create vigenere object
tmp = vigenereCipher()

# Encrypt plaintext
encrypted_message = tmp.encrypt(plaintext, key)
print(f"The encrypted message is {encrypted_message}")

# Decrypt cipher
decrypted_message = tmp.decrypt(encrypted_message, key)
print(f"The decrypted message is {decrypted_message}")
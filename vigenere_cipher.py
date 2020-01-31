import string
import math
import re
import shift_cipher

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
	# Find the length of the unknown key
	def findKeyLength(self, cipher):
		cipher = re.sub(r"[^A-Z]+", "", cipher.upper())
		potential_key_length = 0
		potential_key_sum = 0
		for i in range(1, len(cipher)):
			current = [cipher[index] for index, value in enumerate(cipher) if index % i == 0]
			current_text = "".join(current)
			sc = shift_cipher.shiftCipher()
			broken = sc.break_shift(current_text)
			print(f"Iteration {i}, sum={broken['sum']}")
			if broken["sum"] > potential_key_sum:
				potential_key_sum = broken["sum"]
				potential_key_length = i
		print(f"Potential key length is {potential_key_length}, ({potential_key_sum})")

# Plaintext and key
plaintext = "WE, THEREFORE, THE REPRESENTATIVES OF THE UNITED STATES OF AMERICA, IN GENERAL CONGRESS, ASSEMBLED, APPEALING TO THE SUPREME JUDGE OF THE WORLD FOR THE RECTITUDE OF OUR INTENTIONS, DO, IN THE NAME, AND BY AUTHORITY OF THE GOOD PEOPLE OF THESE COLONIES, SOLEMNLY PUBLISH AND DECLARE, THAT THESE UNITED COLONIES ARE, AND OF RIGHT OUGHT TO BE FREE AND INDEPENDENT STATES, THAT THEY ARE ABSOLVED FROM ALL ALLEGIANCE TO THE BRITISH CROWN, AND THAT ALL POLITICAL CONNECTION BETWEEN THEM AND THE STATE OF GREAT BRITAIN, IS AND OUGHT TO BE TOTALLY DISSOLVED, AND THAT AS FREE AND INDEPENDENT STATES, THEY HAVE FULL POWER TO LEVY WAR, CONCLUDE PEACE, CONTRACT ALLIANCES, ESTABLISH COMMERCE, AND TO DO ALL OTHER ACTS AND THINGS WHICH INDEPENDENT STATES MAY OF RIGHT DO. AND FOR THE SUPPORT OF THIS DECLARATION, WITH A FIRM RELIANCE ON THE PROTECTION OF DIVINE PROVIDENCE, WE MUTUALLY PLEDGE TO EACH OTHER OUR LIVES, OUR FORTUNES AND OUR SACRED HONOR."
key = "UNITEDSTATES"

# Create vigenere object
tmp = vigenereCipher()

# Encrypt plaintext
encrypted_message = tmp.encrypt(plaintext, key)
print(f"The encrypted message is {encrypted_message}")

# Decrypt cipher
decrypted_message = tmp.decrypt(encrypted_message, key)
print(f"The decrypted message is {decrypted_message}")

tmp.findKeyLength(encrypted_message)
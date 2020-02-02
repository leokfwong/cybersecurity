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
		sum_array = []
		for i in range(1, int(len(cipher) / 50)):
			current = [cipher[index] for index, value in enumerate(cipher) if index % i == 0]
			current_text = "".join(current)
			sc = shift_cipher.shiftCipher()
			broken = sc.break_shift(current_text)
			print(f"Iteration {i}, sum={broken['sum']}")
			if i <= len(cipher) / 2:
				sum_array.append(broken["sum"])
		
		diff_array = [abs(x - ENG_PROBABILITY) for x in sum_array]
		top = sorted(range(len(diff_array)), key=lambda k: diff_array[k])[:5]
		top = [x + 1 for x in top]
		print(top)
		min_length = min(top)
		print(f"Potential key length is {min_length}")	

def readTxtString(path):
	with open(path, "r") as f:
		plaintext = f.read().replace("\n", "")
		plaintext = re.sub(r'\s+', ' ', plaintext)
		return plaintext


# Plaintext and key
plaintext = "WE, THEREFORE, THE REPRESENTATIVES OF THE UNITED STATES OF AMERICA, IN GENERAL CONGRESS, ASSEMBLED, APPEALING TO THE SUPREME JUDGE OF THE WORLD FOR THE RECTITUDE OF OUR INTENTIONS, DO, IN THE NAME, AND BY AUTHORITY OF THE GOOD PEOPLE OF THESE COLONIES, SOLEMNLY PUBLISH AND DECLARE, THAT THESE UNITED COLONIES ARE, AND OF RIGHT OUGHT TO BE FREE AND INDEPENDENT STATES, THAT THEY ARE ABSOLVED FROM ALL ALLEGIANCE TO THE BRITISH CROWN, AND THAT ALL POLITICAL CONNECTION BETWEEN THEM AND THE STATE OF GREAT BRITAIN, IS AND OUGHT TO BE TOTALLY DISSOLVED, AND THAT AS FREE AND INDEPENDENT STATES, THEY HAVE FULL POWER TO LEVY WAR, CONCLUDE PEACE, CONTRACT ALLIANCES, ESTABLISH COMMERCE, AND TO DO ALL OTHER ACTS AND THINGS WHICH INDEPENDENT STATES MAY OF RIGHT DO. AND FOR THE SUPPORT OF THIS DECLARATION, WITH A FIRM RELIANCE ON THE PROTECTION OF DIVINE PROVIDENCE, WE MUTUALLY PLEDGE TO EACH OTHER OUR LIVES, OUR FORTUNES AND OUR SACRED HONOR. Mr. Bennet was among the earliest of those who waited on Mr. Bingley. He had always intended to visit him, though to the last always assuring his wife that he should not go; and till the evening after the visit was paid she had no knowledge of it. It was then disclosed in the following manner. Observing his second daughter employed in trimming a hat, he suddenly addressed her with: I am sorry to hear that; but why did not you tell me that before? If I had known as much this morning I certainly would not have called on him. It is very unlucky; but as I have actually paid the visit, we cannot escape the acquaintance now.” The astonishment of the ladies was just what he wished; that of Mrs. Bennet perhaps surpassing the rest; though, when the first tumult of joy was over, she began to declare that it was what she had expected all the while. “How good it was in you, my dear Mr. Bennet! But I knew I should persuade you at last. I was sure you loved your girls too well to neglect such an acquaintance. Well, how pleased I am! and it is such a good joke, too, that you should have gone this morning and never said a word about it till now.” “Now, Kitty, you may cough as much as you choose,” said Mr. Bennet; and, as he spoke, he left the room, fatigued with the raptures of his wife. “What an excellent father you have, girls!” said she, when the door was shut. “I do not know how you will ever make him amends for his kindness; or me, either, for that matter. At our time of life it is not so pleasant, I can tell you, to be making new acquaintances every day; but for your sakes, we would do anything. Lydia, my love, though you are the youngest, I dare say Mr. Bingley will dance with you at the next ball.”"
key = "UNITEDSTATES"

#plaintext = readTxtString("test.txt")
#key = "MAMBA"
print(len(plaintext))

# Create vigenere object
tmp = vigenereCipher()

# Encrypt plaintext
encrypted_message = tmp.encrypt(plaintext, key)
#print(f"The encrypted message is {encrypted_message}")
print(len(encrypted_message))

# Decrypt cipher
decrypted_message = tmp.decrypt(encrypted_message, key)
#print(f"The decrypted message is {decrypted_message}")
print(len(decrypted_message))

encrypted_message = readTxtString("cipher.txt")
tmp.findKeyLength(encrypted_message)

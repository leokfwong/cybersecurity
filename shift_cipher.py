import string
from collections import Counter

# Initialize constants
ALPHABET = string.ascii_uppercase
eng_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
ENG_PROBABILITY = 0.065

class shiftCipher:
	"""
	Object containing methods to encrypt and decrypt a shift cipher given a message and a shift length k.
	Can also break any shift cipher without knowing k given that the encrypted message is long enough.
	"""
	# Encrypt message by shifting k positions
	def encrypt(self, message, k):
		k %= 26
		trans = str.maketrans(ALPHABET, ALPHABET[k:] + ALPHABET[:k])
		return message.upper().translate(trans)

	# Decrypt message by shifting -k positions
	def decrypt(self, message, k):
		k %= 26
		trans = str.maketrans(ALPHABET, ALPHABET[-k:] + ALPHABET[:-k])
		return message.upper().translate(trans)

	# Break cipher by frequency analysis
	def break_shift(self, enc_msg, verbose=False):
		# Get counts of each letter of the alphabet of encrypted message
		counts = Counter(enc_msg)
		# Initialize minimum difference between sum and English probability
		min_diff = 1
		most_likely_k = 0
		most_likely_sum = 0
		# Iterate through each letter of the alphabet (testing every k shifts)
		for k in range(len(ALPHABET)):
			# Initialize sum
			sum = 0
			plain_message = self.decrypt(enc_msg, k)
			# Iterate through every letter to calculate frequency
			for i in range(len(ALPHABET)):
				# Probability of letter_i based on English language
				f = eng_freq[i] / 100
				# Probability of letter_i + shift k from corpus
				h = counts[self.encrypt(ALPHABET[i], k)] / len(enc_msg)
				# Add product to sum of probabilities
				sum += f * h
			if verbose:
				print(f"k = {k}; sum = {str(sum)[:10]}; msg = {plain_message[:30]}...")
			#print(f"Decrypted message = {plain_message}")
			# Check if sum is closer to 0.065 for given k
			diff = abs(sum - ENG_PROBABILITY)
			if diff < min_diff:
				# If closer, update most likely k
				min_diff = diff
				most_likely_k = k
				most_likely_sum = sum

		# Return most likely k and decrypted message
		plain_message = self.decrypt(enc_msg, most_likely_k)
		if verbose:
			print(f"The most likely k is {most_likely_k}")
			print(f"Decrypted message = {plain_message}")

		d = dict()
		d["k"] = most_likely_k
		d["sum"] = most_likely_sum
		d["msg"] = plain_message

		return d

'''
# Import data
# Comment out to load text file
with open("61195-0.txt", "r"") as f:
    plaintext = f.read().replace("\n", "")

# Plaintext to encrypt
plaintext = "THIS IS A HIDDEN MESSAGE"
plaintext = "SHIFTCIPHERSARESIMPLE"
plaintext = "SHIFTCIPHERSARESIMPLEBUTNEEDSTOBELONGENOUGH"

# Create object
sc = shiftCipher()

# Encrypt plaintext with a shift by 7
enc_message = sc.encrypt(plaintext, 7)
print(f"Encrypted message: {enc_message}")
dec_message = sc.decrypt(enc_message, 7)
print(f"Decrypted message: {dec_message}")

# Examples of how to break encrypted messages
enc_msg_1 = "WIVHLVETPRERCPJZJTRESVLJVUFEFKYVIKPGVJFWTZGYVIJKFFSLKZKZJEFKLJLRCCPRJJZDGCVRJZKZJNZKYJYZWKTZGYVIJDREPFWKYVJVFKYVITZGYVIJNZCCRGGVRIYVIVZEKYVEVOKWVNDFEKYJ"
broken = sc.break_shift(enc_msg_1, verbose=True)
'''
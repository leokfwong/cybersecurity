import math

def debruijn(k, n):
	# Initialize alphabet
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	# alphabet = "0123456789"
	# Get sequence size
	size = k**n
	# Generate lists
	bottom = list(alphabet[:k] * math.ceil(size/k))
	top = sorted(bottom)
	tracker = list(range(size))
	# Generate mapping
	mapping = []
	for i in range(k):
		mapping.extend([x for x in list(range(size)) if x % k == i])
	# Create list to store result
	indices = []
	# While there are indices we haven't encountered yet
	while len(tracker) > 0:
		# Create a new cycle starting at j
		j = tracker[0]
		start = j
		# While the mapping of j does not map back to start
		while mapping[j] != start:
			# Add the index and remove it from the tracker
			indices.append(j)
			tracker.remove(j)
			# Update j to the index it maps to
			j = mapping[j]
		# Add index and remove from tracker
		indices.append(j)
		tracker.remove(j)

	# Find the characters at each index of result
	result = [top[x] for x in indices]
	# Return list
	return result

result = debruijn(10, 4)
print("".join(result))
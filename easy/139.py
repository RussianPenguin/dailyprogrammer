import re
import collections
import sys

def isPangram(string):
	alphaFinder = re.compile('[a-z]')
	alpha = alphaFinder.findall(string)
	counter = collections.Counter(alpha)
	#print counter
	#print counter.keys()
	#print counter.values()
	#print counter.most_common(3)
	return len(counter) == 26, counter
	
if __name__ == '__main__':
	strings = [raw_input().strip().lower() for _ in range(input())]

	for item in strings:
		is_pangram, letters = isPangram(item)
		print is_pangram
		print " ".join("%s:%d" % (x, letters[x]) for x in sorted(letters))

	#print strings

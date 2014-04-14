import re

def disemvoweler(string):
	vowels = re.compile('(?i)[aeiou]')
	notVowels = re.compile('(?i)[^aeiou]')

	return vowels.sub('', string),  notVowels.sub('', string)


if __name__ == '__main__':
	line = re.sub('\W', '', raw_input())
	result = disemvoweler(line)

	print result[0]
	print result[1]






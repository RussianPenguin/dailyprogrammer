# -*- encoding: utf8 -*-

braile = {
	'100100': 'a',
	'101000': 'b',
	'110000': 'c',
	'110100': 'd',
	'100100': 'e',
	'111000': 'f',
	'111100': 'g',
	'101100': 'h',
	'011000': 'i',
	'011100': 'j',

	'100110': 'k',
	'101010': 'l',
	'110010': 'm',
	'110110': 'n',
	'100110': 'o',
	'111010': 'p',
	'111110': 'q',
	'101110': 'r',
	'011010': 's',
	'011110': 't',

	'100111': 'u',
	'101011': 'v',
	'110011': 'x',
	'110111': 'y',
	'100111': 'z',

	'011101': 'w'
}

file = open('input.txt', 'r')

input = []

for line in file.readlines():
	idx = 0

	for char in line:
		if len(input) == idx:
			input.append('')

		if char == ' ':
			idx = idx+1
		elif char == 'O' or char == '.':
			input[idx] += '1' if char == 'O' else '0'

print input

output = ''

for x in input:
	if len(x) == 6 and x in braile:
		output += braile[x]
	
print output
file.close()


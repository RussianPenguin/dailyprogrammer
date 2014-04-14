import imp

e149 = imp.load_source('e149', '../easy/149.py')

dictionary = []

# read dictionary and remove non-characters
with open('./150/enable1.txt') as f:
	def preparation(line):
		str = ''.join(e for e in line if e.isalnum())
		return str, e149.disemvoweler(str)

	dictionary = map(preparation, f.readlines())

puzzle = (raw_input(), raw_input())

def solve(puzzle, resultString):
	# search pattern for puzzle
	# pattern shold be part of puzzle

	puz0len = len(puzzle[0])
	puz1len = len(puzzle[1])

	for item in dictionary:
		# system variables
		i0len = len(item[1][0])
		i1len = len(item[1][1])

		if i0len <= puz0len and i1len <= puz1len and item[1][0] == puzzle[0][:(i0len)] and item[1][1] == puzzle[1][:(i1len)]:
			
			puz0last = puzzle[0][i0len:]
			puz1last = puzzle[1][i1len:]

			if len(puz0last) > 0 or len(puz1last) > 0:
				solve((puz0last, puz1last), resultString + ' ' + item[0])
			else:
				print resultString + ' ' + item[0]
		

solve(puzzle, '')


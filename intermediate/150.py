import imp
import os.path
import sys

print os.path.dirname(__file__)
basepath = os.path.dirname(__file__)

print os.path.abspath(os.path.join(basepath, '..', 'easy/149.py'))
e149 = imp.load_source('e149', os.path.abspath(os.path.join(basepath, '..', 'easy/149.py')))

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

		if i0len > puz0len or i1len > puz1len:
			continue

		if i0len <= puz0len and i1len <= puz1len and item[1][0] == puzzle[0][(-i0len):] and item[1][1] == puzzle[1][(-i1len):]:
			
			puz0last = puzzle[0][:-i0len]
			puz1last = puzzle[1][:-i1len]

			if len(puz0last) > 0 or len(puz1last) > 0:
				for solution in solve((puz0last, puz1last), item[0] + ' ' + resultString):
					yield solution
			else:
				yield item[0] + ' ' + resultString
		

if __name__ == '__main__':

	for solution in solve(puzzle, ''):
		print solution


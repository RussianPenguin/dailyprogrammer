# -*- encoding: utf8 -*-

def drop_snow(tube):
	len_of_tube = len(tube)
	tube = tube.replace(' ', '')
	return tube.rjust(len_of_tube, ' ')

if __name__ == '__main__':
	size = input()
	matrix = []
	for x in range(0, size):
		matrix.append(raw_input()[:size].ljust(size, ' '))

	output = map(lambda x: '#'.join(map(drop_snow, ''.join(x).split('#'))), map(list, zip(*matrix)))
	print '-' * size
	for item in map(lambda x: ''.join(x), map(list, zip(*output))):
		print item
	

# -*- encoding: utf8 -*-

if __name__ == '__main__':
	width, stump, needles = raw_input().split()
	width = int(width)

	tree = []
	for i in range(1, width+1, 2):
		distance = (width - i) / 2
		print ' ' * distance + needles * i + ' ' * distance
	else:
		distance = (width - 3) / 2
		print ' ' * distance + stump * 3 + ' ' * distance

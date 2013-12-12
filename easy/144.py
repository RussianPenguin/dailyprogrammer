# -*- encoding: utf8 -*-

if __name__ == '__main__':
	items = [raw_input().split() for _ in range(int(input()) * 2)]
	measure = {}
	for item in items:
		if item[0] in measure and int(item[1]) - int(measure[item[0]]):
			print "%s %+d" % (item[0], (int(item[1]) - int(measure[item[0]])))
		else:
			measure[item[0]] = item[1]

# -*- encoding: utf8 -*-

import random
import datetime

if __name__ == '__main__':
	simulation = int(input())	

	tactics = [0, 0]

	for step in xrange(0, simulation):
		random.seed(datetime.datetime.now())
		doors = ['car', 'goal', 'goal']

		random.shuffle(doors)

		select = random.randint(0, 2)
		
		# the trick for pick door to open
		opened_door = select
		while opened_door == select or doors[opened_door] == 'car':
			opened_door = random.randint(0, 2)

		other_door = list(set(range(3)) - set([select, opened_door]))[0]
		if doors[select] == 'car':
			tactics[0] += 1
		elif doors[other_door] == 'car':
			tactics[1] += 1

	print tactics

# -*- encoding: utf8 -*-

import math

if __name__ == '__main__':
	circles = map(lambda x: float(x), raw_input().split())
	if len(circles) != 4:
		exit(1)

	# calc d for area

	d = math.sqrt((circles[0]-circles[2]) ** 2 + (circles[1] - circles[3]) ** 2)

	# calc theta 
	# theta = 2*arccos(d/R)
	
	two_circle_area = 2*math.pi
	
	# calc subareas olny if circles intersect
	if d < 2:
		theta = 2.0 * math.acos(d/2)
		sub_area = (theta - math.sin(theta))
		two_circle_area -= sub_area

	print two_circle_area

import math

if __name__ == '__main__':
	n, r = map(float, raw_input().split())
	print "%.3f" % (2*r*math.sin(math.pi/n)*n)

import math

if __name__ == '__main__':
	data = [map(float, raw_input().split()) for _ in range(2)]
	print "%.4f" % ((data[0][0] * data[1][0])/((data[0][1] - data[1][1])**2 + (data[0][2] - data[1][2])**2))

import math
import sys

def read():
	points = {}
	raw = raw_input()
	while raw:
		x, y = map(float, raw.split())
		points[x] = y
		raw = raw_input()
	return points

if __name__ == '__main__':
	points = read()
	real = []
	img = []
	complex = []
	N = len(points)
	
	#print points

	for m in range(N):
		n = 0
		real.append(0.0)
		img.append(0.0)
		complex.append(0.0)
		for x in sorted(points):
			y = points[x]
			real[m] += y*math.cos(2*math.pi*m*n/N)
			img[m] += y*math.sin(2*math.pi*m*n/N)
			complex[m] += y*math.e**(-2j*math.pi*n*m/N)
			n += 1
		
		print "x(%d) = %f%+fj" % (m, real[m], -img[m]), complex[m]

	signal = []
	for n in range(N):
		signal.append(0.0)
		m = 0
		while  m < N:
			signal[n] += complex[m]*math.e**(2j*n*m*math.pi/N)
			m += 1
		signal[n] /= N
		#print signal[n]
		amplitude = math.sqrt(real[n]**2 + img[n]**2)/N
		phase = math.atan2(img[n], real[n])
		#print "amplitude: %f, phase: %f, complex form:" % (amplitude, phase), signal[n]
		sys.stdout.write("%+f*sin(%d*t%+f)" % (amplitude, n, phase))
		#sys.stdout.write("%+f*sin(2*pi*%d*x%+f)" % (amplitude, n, phase))

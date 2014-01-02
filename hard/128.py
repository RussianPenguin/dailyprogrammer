import math
import sys
import numpy

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

	# three different compute of DFT
	for m in range(N):
		n = 0
		real.append(0.0)
		img.append(0.0)
		complex.append(0.0)
		for x in sorted(points):
			y = points[x]

			# trigonometric form of dft
			real[m] += y*math.cos(2*math.pi*m*n/N)
			img[m] -= y*math.sin(2*math.pi*m*n/N)
			
			#complex form of dft
			complex[m] += y*math.e**(-2j*math.pi*n*m/N)
			n += 1
		
		#print "x(%d) = %f%+fj" % (m, real[m], img[m]), complex[m]

	# dft fron numpy package
	dft = numpy.fft.fft([points[x] for x in sorted(points)])

	# find three differences
	#for idx in range(len(dft)):
	#	print dft[idx], complex[idx], real[idx], img[idx]

	# creation of an analytical equation
	equation = ''

	for k in range(N):
		amplitude = math.sqrt(complex[k].real**2 + complex[k].imag**2)/N
		phase = math.atan2(complex[k].imag, complex[k].real)

		# freq for k numbered point calculated like
		# f = k/T where T is number of points
		equation += "%+f*cos(%f*x%+f)" % (amplitude, 2.0*math.pi*k/10.0, phase)

	print "Analytical form: %s" % equation
	# try to create equation formed as A*sin(a*x+fi_1)+B*cos(b*x+fi_2) 

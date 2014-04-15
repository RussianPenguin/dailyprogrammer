import math

def trinome(n, k, l):
	n_f = math.factorial(n)
	k_f = math.factorial(k)
	l_f = math.factorial(l)

	n_k_l_f = math.factorial(n-k-l)

	return n_f/(k_f*l_f*n_k_l_f)

layer = int(raw_input())

pyramid = []

width = 0

for k in range(0, layer+1):
	row = []
	for l in range(layer-k+1):
		row.append(trinome(layer, k, l))
	pyramid.insert(0, ' '.join(map(str, row)))
	if len(pyramid[0]) > width:
		width = len(pyramid[0])

for x in pyramid:
	print x.center(width)

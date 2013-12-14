# -*- encoding: utf8 -*-
import math

def modular_exp(b, n, k):
	t = 1
	while t <= n:
		t *= 2
	else:
		t /= 2
	r = 1

	while True:
		if n >= t:
			r = b*r % k
			n = n - t
		t /= 2
		if t >= 1:
			r = r ** 2 % k
			continue
		break
	return r
			
	

def bbp_sum(d, j):
	sum = 0.0

	for k in xrange(d+1):
		eight_k_j = float(8*k+j)
		fraction = (modular_exp(16, d - k, eight_k_j)) / eight_k_j
		sum += fraction

	sum = sum - int(sum)

	k = d+1
	sigma = 1e-15
	while True:
		eight_k_j = float(8*k + j)
		fraction = 16.0 ** (d - k) / eight_k_j
		if fraction < sigma:
			break
		sum += fraction
		k += 1

	sum = sum - int(sum)
	print j, sum
	return sum
	

def bbp(d):
	result = 4*bbp_sum(d, 1) - 2*bbp_sum(d, 4) - bbp_sum(d, 5) - bbp_sum(d, 6)
	result = result - math.floor(result)
	digit = result * 16
	hex_str = ''
	for i in range(6):
		result = result * 16.0
		hex_str += '%X' % int(result)
		result = result - math.floor(result)
	print hex_str
	return int(digit)

if __name__ == '__main__':
	print '%X' % bbp(1000000)

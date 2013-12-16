# -*- encoding: utf8 -*-
import math
import multiprocessing
import socket
import sys

def bbp_sum(j, d):

	sum1 = 0.0
	k = 0
	while k <= d:
		eight_k_j = 8*k+j
		sum1 = (sum1 + float(pow(16, d - k, eight_k_j)) / eight_k_j) % 1.0
		k += 1

	k = d+1
	sigma = 1e-25

	sum2 = 0.0
	while True:
		eight_k_j = float(8*k + j)
		sum2_temp = sum2 + pow(16.0, d - k) / eight_k_j

		if math.fabs(sum2 - sum2_temp) < sigma:
			break
		sum2 = sum2_temp

		k += 1

	print j, sum1+sum2
	return (sum1+sum2) % 1.0
	
def calc_sd(x):
	return x[0]*bbp_sum(x[1], x[2])

def bbp(d):
	pool = multiprocessing.Pool(processes=4)
	matrix = [(4, 1 ,d), (-2, 4, d), (-1, 5, d), (-1, 6, d)]
	result = pool.map(calc_sd, matrix)
	pool.close()
	pool.join()
	result = reduce(lambda x, y: x+y, result)
	#result = 4*bbp_sum(d, 1) - 2*bbp_sum(d, 4) - bbp_sum(d, 5) - bbp_sum(d, 6)
	result = result - math.floor(result)
	digit = result * 16
	hex_str = ''
	for i in range(10):
		result = result * 16.0
		hex_str += '%X' % int(result)
		result = result - math.floor(result)
	print hex_str
	return int(digit)

if __name__ == '__main__':

	BUFFER_SIZE=50
	bind_to = sys.argv[1].split(':')


	print bind_to
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((bind_to[0], int(bind_to[1])))
	s.listen(1)

	while True:
		conn, addr = s.accept()
		
		data = conn.recv(BUFFER_SIZE)
		while data:
			data = data.strip()
			#print data
			if data == 'kill':
				exit(0)
			if data.isdigit():
				conn.send("%X\n" % bbp(int(data) - 1))
			data = conn.recv(BUFFER_SIZE)

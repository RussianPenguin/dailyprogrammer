import sys
import threading
import socket

class worker(threading.Thread):
	def __init__(self, ip, port, generator):
		super(worker,self).__init__()
		self.ip = ip
		self.port = port
		self.generator = generator

	def run(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.ip, self.port))
			for current_pos_in_pi in self.generator:
				s.send("%d" % current_pos_in_pi)
				response = s.recv(1024)
				print "%d:%X" % (current_pos_in_pi, int(response, 16))
			s.send('kill')
			s.close()
		finally:
			pass



if __name__ == '__main__':
	servers = [raw_input().split(':') for _ in range(4)]
	digits = int(raw_input())

	generator = iter(xrange(digits))

	for server in servers:
		t = worker(server[0], int(server[1]), generator)
		t.start()

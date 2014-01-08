if __name__ == '__main__':
	score = int(raw_input())
	max_multiply = score/3

	#out = []
	for i in xrange(max_multiply):
		for j in xrange(max_multiply):
			for k in xrange(max_multiply):
				for m in xrange(max_multiply):
					#out.append(i*3+j*6+k*7+m*8)
					if i*3+j*6+k*7+m*8 == score:
						print "Valid Score"
						exit(0)
						#pass
	print "Invalid Score"
	#print set(out)

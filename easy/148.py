def rotate(from_pos, to_pos, size):
	if from_pos > to_pos:
		return (size - from_pos) + to_pos
	elif to_pos > from_pos:
		return to_pos - from_pos
	else:
		return size

if __name__ == '__main__':
	size, first, second, third = map(int, raw_input().split())

	total = 0

	# Spin the lock a full 2 times clockwise, and continue rotating it to the code's first digit.
	total += size*2 + rotate(0, first, size)
	#Spin the lock a single time counter-clockwise, and continue rotating to the code's second digit.
	total += size + rotate(second, first, size)
	#Spin the lock clockwise directly to the code's last digit.
	total += rotate(second, third, size)

	print total

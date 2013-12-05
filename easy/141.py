# -*- encoding: utf8 -*-

def fletcher(text):
	sum1 = 0
	sum2 = 0

	for c in text:
		sum1 = (sum1 + ord(c)) % 255
		sum2 = (sum1 + sum2) % 255

	return sum2 << 8 | sum1

if __name__ == '__main__':
	text = map(fletcher, [raw_input() for i in range(input())])
	for idx in range(len(text)):
		print idx + 1, "%4X" % text[idx]

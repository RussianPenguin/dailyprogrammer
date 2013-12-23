import re
import sys

keypad = {
	'0': '',
	'1': '',
	'2': 'ABC',
	'3': 'DEF',
	'4': 'GHI',
	'5': 'JKL',
	'6': 'MNO',
	'7': 'PQRS',
	'8': 'TUV',
	'9': 'WXYZ',
}

source = './brit-a-z.txt'

if __name__ == '__main__':

	# replace num sequence by its content and length like [<sequence>]{1,<max count>}
	def repl_callback(r):
		#print r.group(0), r.group(1)
		num = r.group(1)
		count = len(r.group(0))
		if num in keypad and len(keypad[num]):
			return "[%s]{1,%d}" % (keypad[num].lower(), count)
		return ''

	number = re.sub('(\D)', '', raw_input())
	regexp = re.sub(r"(\d)\1*", repl_callback, number)

	#print number, regexp

	finder = re.compile(r"^%s." % regexp)

	with open(source, 'r') as file:
		pass
		for line in iter(file.readline, ''):
			if finder.match(line):
				sys.stdout.write(line)

		 

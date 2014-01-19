import re
import sys
import array

class Compiler:
	def __init__(self, lines):
		self.instructions = list([])
		self.lines = lines

		self.instructions.append(('^\s*$', lambda x: []))
		self.instructions.append(('^\s*;.*$', lambda x: []))

		# and
		self.instructions.append(('^\s*and\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x00, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*and\s+\[(\d+)\]\s+(\d+)', lambda x: [0x01, x.group(1), x.group(2)]))		

		# or
		self.instructions.append(('^\s*or\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x02, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*or\s+\[(\d+)\]\s+(\d+)', lambda x: [0x03, x.group(1), x.group(2)]))

		# xor
		self.instructions.append(('^\s*xor\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x04, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*xor\s+\[(\d+)\]\s+(\d+)', lambda x: [0x05, x.group(1), x.group(2)]))

		# not
		self.instructions.append(('^\s*not\s+\[(\d+)\]', lambda x: [0x06, x.group(1)]))

		# mov
		self.instructions.append(('^\s*mov\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x07, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*mov\s+\[(\d+)\]\s+(\d+)', lambda x: [0x08, x.group(1), x.group(2)]))

		# random
		self.instructions.append(('^\s*random\s+\[(\d+)\]', lambda x: [0x09, x.group(1)]))

		# add
		self.instructions.append(('^\s*add\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x0a, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*add\s+\[(\d+)\]\s+(\d+)', lambda x: [0x0b, x.group(1), x.group(2)]))
		
		# sub
		self.instructions.append(('^\s*sub\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x0c, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*sub\s+\[(\d+)\]\s+(\d+)', lambda x: [0x0d, x.group(1), x.group(2)]))

		# jmp
		self.instructions.append(('^\s*jmp\s+\[(\d+)\]', lambda x: [0x0e, x.group(1)]))
		self.instructions.append(('^\s*jmp\s+(\d+)', lambda x: [0x0f, x.group(1)]))

		# jz
		self.instructions.append(('^\s*jz\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x10, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*jz\s+\[(\d+)\]\s+(\d+)', lambda x: [0x11, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*jz\s+(\d+)\s+\[(\d+)\]', lambda x: [0x12, x.group(1), x.group(2)]))
		self.instructions.append(('^\s*jz\s+(\d+)\s+(\d+)', lambda x: [0x13, x.group(1), x.group(2)]))

		# jeq
		self.instructions.append(('^\s*jeq\s+\[(\d+)\]\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x14, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jeq\s+(\d+)\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x15, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jeq\s+\[(\d+)\]\s+\[(\d+)\]\s+(\d+)', lambda x: [0x16, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jeq\s+(\d+)\s+\[(\d+)\]\s+(\d+)', lambda x: [0x17, x.group(1), x.group(2), x.group(3)]))

		# jls
		self.instructions.append(('^\s*jls\s+\[(\d+)\]\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x18, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jls\s+(\d+)\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x19, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jls\s+\[(\d+)\]\s+\[(\d+)\]\s+(\d+)', lambda x: [0x1a, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jls\s+(\d+)\s+\[(\d+)\]\s+(\d+)', lambda x: [0x1b, x.group(1), x.group(2), x.group(3)]))

		# jgt
		self.instructions.append(('^\s*jgt\s+\[(\d+)\]\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x1c, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jgt\s+(\d+)\s+\[(\d+)\]\s+\[(\d+)\]', lambda x: [0x1d, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jgt\s+\[(\d+)\]\s+\[(\d+)\]\s+(\d+)', lambda x: [0x1e, x.group(1), x.group(2), x.group(3)]))
		self.instructions.append(('^\s*jgt\s+(\d+)\s+\[(\d+)\]\s+(\d+)', lambda x: [0x1f, x.group(1), x.group(2), x.group(3)]))

		# halt
		self.instructions.append(('^\s*halt', lambda x: [0xff]))

		# aprint
		self.instructions.append(('^\s*aprint\s+\[(\d+)\]', lambda x: [0x20, x.group(1)]))
		self.instructions.append(('^\s*aprint\s+(\d+)', lambda x: [0x21, x.group(1)]))

		# aprint
		self.instructions.append(('^\s*dprint\s+\[(\d+)\]', lambda x: [0x22, x.group(1)]))
		self.instructions.append(('^\s*dprint\s+(\d+)', lambda x: [0x23, x.group(1)]))


	def compile(self):
		for instruction in self.lexer():
			for pattern in self.instructions:
				match = re.search(pattern[0], instruction, re.IGNORECASE)
				if match:
					yield map(int, pattern[1](match))
					break
			else:
				raise Exception("No such instructions for pattern: %s" % (instruction))

	def lexer(self):
		for line in self.lines:
			yield line

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as input:
		out = None
		if 2 in sys.argv:
			out = open(sys.argv[2], 'w+b')

		lines = iter(input.readline, '')
		compiler = Compiler(lines)
		for bytes in compiler.compile():
			print " ".join(map(lambda x: "0x%02X" % x, bytes))
			if out:
				array.array('B', bytes).tofile(out)

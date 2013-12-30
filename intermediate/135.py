"""

Define grammar and rules for output

S := const
S := (S)
S := not S
S := S and S
S := S or S

Rules:

Out(S) := not S
Out(not S) := S
OUT(S and S) := not S or not S
Out(S or S) := not S and not S

"""


class Tokenizer:

	def __init__(self, input):
		self.iter = iter(self.tokenize(input))
		self.last = None
		self.has_last = False

	def __iter__(self):
		return self

	def next(self):
		if self.has_last:
			item = self.last
			self.has_last = False
			self.last = None # Don't hang on to it.
		else:
			item = self.iter.next()
		return item

	def pushback(self, item):
		if self.has_last:
			raise Exception("I'm full!")
		self.last = item
		self.has_last = True 

	def createToken(self, string):
		type = 'const'
		if string.lower() == 'and':
			type = 'and'
		if string.lower() == 'or':
			type = 'or'
		if string.lower() == 'not':
			type = 'not'
		if string.lower() == '(':
			type = 'LP'
		if string.lower() == ')':
			type = 'RP'

		return {'value': string, 'type': type}

	def tokenize(self, input):
		token = ''

		for c in input:
			if c.isalpha():
				token += c
			else:
				if len(token):
					yield self.createToken(token)
				if c == '(' or c == ')':
					yield self.createToken(c)
				token = ''
		else:
			if len(token):
				yield self.createToken(token)


def normalOutput(input):
	output = ''
	for token in input:
		if token['type'] == 'RP':
			print token
			return output
		if token['type'] == 'const':
			output += "%s" % (token['value'])
			return output
		if token['type'] == 'and':
			output += " and %s" % (normalOutput(input))
		if token['type'] == 'or':
			output += " or %s" % (normalOutput(input))
		if token['type'] == 'not':
			output += "not %s" % (normalOutput(input))
		if token['type'] == 'LP':
			output += "(%s)" % (normalOutput(input))
	return output

def normalOrder(input):
	output = ''
	token = input.next()
	while token:
		if token['type'] == 'not':
			try:
				nextToken = input.next()
				if nextToken['type'] == 'LP':
					input.pushback(nextToken)
					output += normalOrder(input)
				else:
					output += "not %s" % nextToken['value']
			except StopIteration:
				print "syntax error"
				pass

		if token['type'] == 'const':
			try:
				operator = input.next()
				if operator['type'] == 'or':
					return "%s or %s" % (token['value'], normalOrder(input))
				if operator['type'] == 'and':
					return "%s and %s" % (token['value'], normalOrder(input))
				if operator['type'] == 'RP':
					return "%s" % token['value']
			except StopIteration:
				return token['value']
		if token['type'] == 'LP':
			return "(%s)" % normalOrder(input)
		if token['type'] == 'and': 
			output += " %s %s" % ('and', normalOrder(input))
		if token['type'] == 'or':
			output += " %s %s" % ('or', normalOrder(input))

		try:
			token = input.next()
		except StopIteration:
			break
	return output
		
def deMorgansLaw(input):
	output = ''
	token = input.next()
	while token:
		if token['type'] == 'not':
			try:
				nextToken = input.next()
				if nextToken['type'] == 'LP':
					input.pushback(nextToken)
					output += normalOrder(input)
				else:
					output += "%s" % nextToken['value']
			except StopIteration:
				print "syntax error"
				pass

		if token['type'] == 'const':
			try:
				operator = input.next()
				if operator['type'] == 'or':
					return "not %s and %s" % (token['value'], deMorgansLaw(input))
				if operator['type'] == 'and':
					return "not %s or %s" % (token['value'], deMorgansLaw(input))
				if operator['type'] == 'RP':
					return "not %s" % token['value']
			except StopIteration:
				return "not %s" % token['value']
		if token['type'] == 'LP':
			return "(%s)" % deMorgansLaw(input)
		if token['type'] == 'and': 
			output += " %s %s" % ('or', deMorgansLaw(input))
		if token['type'] == 'or':
			output += " %s %s" % ('and', deMorgansLaw(input))

		try:
			token = input.next()
		except StopIteration:
			break
	return output
		
if __name__ == '__main__':
	input = raw_input()
	while input:
		print "input: %s" % input
		print "output: %s" % deMorgansLaw(Tokenizer(input))
		input = raw_input()

import re

def readConversion():
	string = ''
	conversion = []
	try:
		# obtain conversion pattern
		raw = raw_input()
		while not raw:
			raw = raw_input()

		conversion = map(int, raw.split())

		# obtain string
		string = raw_input()
		while not string:
			string = raw_input()
	finally:
		return conversion, string

def converter(string, outForm, inputForm = -1):
	inputFinder = {
		-1: re.compile('(\S+)'),
		0: re.compile('((?:^|[A-Z])[a-z]*)'),
		1: re.compile('([^_]+)'),
		2: re.compile('([^_]+)')
	}

	outputCompiler = {
		0: lambda x: x[0].lower() + "".join(map(lambda x: x.lower().title(), x[1:])),
		1: lambda x: "_".join(map(lambda x: x.lower(), x)),
		2: lambda x: "_".join(map(lambda x: x.upper(), x))
	}
	
	inputData = inputFinder[inputForm].findall(string)
	outputData = outputCompiler[outForm](inputData)		
	return outputData

if __name__ == '__main__':
	while True:
		conversion, string = readConversion()
		if len(conversion) >= 1:
			print (conversion[::-1])[0]
			print converter(string, *(conversion[::-1]))
		else:
			break

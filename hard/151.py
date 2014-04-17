# solution use http://www.afterthedeadline.com/api.slp
# and https://bitbucket.org/miguelventura/after_the_deadline/

import imp
import sys
import os.path

basepath = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(basepath, '..', 'modules/ATD')))

import ATD

i150 = imp.load_source('i150', os.path.abspath(os.path.join(basepath, '..', 'intermediate/150.py')))

# random key
ATD.setDefaultKey("9WdSTQHB2fg43cHVXZIbjJja5xxHzaMAAt4YJAWRykk=")

puzzle = i150.readPuzzle()

for solution in i150.solve(puzzle, ''):
	errors = ATD.checkDocument(solution)
	if len(errors) == 0:
		print "Solution '%s' is good" % (solution)
	else:
		print "Solution '%s' is bad. Reasons:" % (solution)

		for error in errors:
			print "%s error for: %s **%s**" % (error.type, error.precontext, error.string)
			print "some suggestions: %s" % (", ".join(error.suggestions),)

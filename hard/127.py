# -*- encoding: utf-8 -*- from __future__ import unicode_literals

import codecs
import re

dictionaries = {
	'en': [
		('./127.dict/eng_com.dic', 'latin1'),
		('./127.dict/center.dic', 'utf8'),
		('./127.dict/Ise.dic', 'utf8'),
		('./127.dict/color.dic', 'utf8'),
		('./127.dict/labeled.dic', 'utf8')
	],
	'fr': [('./127.dict/fr.dic', 'utf16')],
	'es': [('./127.dict/es.dic', 'utf16')],
	'de': [('./127.dict/de_neu.dic', 'utf16')],
	'pt': [('./127.dict/portugueseU.dic', 'utf16')]
}

languageMap = {
	'en': 'English',
	'fr': 'French',
	'es': 'Spanish',
	'de': 'German',
	'pt': 'Portuguese'	
}

def occurencesCounter(words, lang):
	crawl = re.compile("^(%s)$" % ("|".join(words)))
	#print ("^(%s)$" % ("|".join(words))), lang
	occurences = 0
	for dict in dictionaries[lang]:
		with codecs.open(dict[0], 'r', encoding=dict[1]) as file:
			#print dict
			for line in file:
				line = line.rstrip("\n")
				
				#if line == u"classé":
				#	print line.encode('utf8')
				
				if crawl.match(line.encode('utf8')):
					occurences += 1
	return occurences

if __name__ == '__main__':
	text = raw_input()
	words = text.split()
	#remove stop-words
	ordinaryWords = filter(lambda word: len(word) > 2, words)
	weights = {}
	for lang in dictionaries:
		occurences = occurencesCounter(ordinaryWords, lang)
		if occurences == 0:
			continue
		weights[float(occurences) / len(ordinaryWords)] = lang

	for weight in sorted(weights, reverse = True):
		print "%s (%.3f%%)" % (languageMap[weights[weight]], weight)
		if weight == 1.0:
			break


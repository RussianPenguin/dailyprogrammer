import re

line = re.sub('\W', '', raw_input())

vovels = re.compile('(?i)[aeiou]')
notVovels = re.compile('(?i)[^aeiou]')

print vovels.sub('', line)
print notVovels.sub('', line)




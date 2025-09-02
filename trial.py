import re
pattern = re.compile('^[0-9]+[a-z]$')
print(pattern.search('794abc'))
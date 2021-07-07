import re

p = re.compile('[aeiou][b-df-hj-np-tv-z][B-DF-HJ-NP-TV-Z]')
matchObj = p.findall('akKebIoTzotZ')
print(matchObj)

'''
[aeiou]
[b-df-hj-np-tv-z]
[B-DF-HJ-NP-TV-Z]
'''

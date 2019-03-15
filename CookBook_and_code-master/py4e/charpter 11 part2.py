import re

fname = open(r'mbox-short.txt')
for line in fname:
    line = line.rstrip()
    x = re.findall('\S+@\S+',line)
    if x != []:
        print(x)
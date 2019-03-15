import re

fname = open('mbox-short.txt')
for line in fname:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)
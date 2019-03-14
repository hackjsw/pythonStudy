ffile = input('Input File:')
files = open(ffile)

a = []
for line in files:
    words = line.split()
    #print(words)
    if len(words) > 3 and words[0] == 'From':
        a.append(words[1])

fb = {}
for x in a:
    fb[x] = fb.get(x, 0) + 1

print(fb)
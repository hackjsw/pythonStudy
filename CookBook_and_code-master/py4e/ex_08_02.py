fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    #print('debug',words)
    if  len(words) > 2 and words[0] == 'From':
        print(words[2])
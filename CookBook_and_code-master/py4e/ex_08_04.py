ffile = open('romeo.txt')
words = []
for line in ffile:
    #print(line)
    word = line.split()
    for i in word:
        words.append(i)

words.sort()
print(words)
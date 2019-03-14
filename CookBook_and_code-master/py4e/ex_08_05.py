ffile = open('mbox-short.txt')
count = 0
for line in ffile:
    word = line.split()
    if len(word) > 3 and word[0] == 'From':
        print(word[1])
        count += 1

print('There were {0} lines in the file with From as the first word'.format(count))
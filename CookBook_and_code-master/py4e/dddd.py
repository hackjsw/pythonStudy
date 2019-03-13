count = 0
testx = 0
a = []
x = 0
sumNum = 0
while x != 'done':
    x = input('Enter a number: ')
#    if x == 'done':
#        break
    try:
        testx = int(x)
    except ValueError:
        print('Invalid input')
        continue
    a.append(x)
    count += 1

for i in a:
    sumNum += int(i)

print(sumNum, count, sumNum / count)
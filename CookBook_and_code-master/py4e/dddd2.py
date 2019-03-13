count = 0
sunNum = 0
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        testx = int(x)
    except:
        print('Invalid input')
        continue

    count += 1
    sunNum += testx

print(sunNum, count, sunNum / count)
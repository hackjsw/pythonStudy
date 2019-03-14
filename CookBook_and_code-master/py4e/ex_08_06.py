z = []
while True:
    x = input('Enter a number:')
    if x == 'done':
        break
    try:
        z.append(float(x))
    except:
        print('invalid input')
        continue

print('Maximum:',max(z),'\n','Minmun:',min(z))
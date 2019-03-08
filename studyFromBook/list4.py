spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
for i in spam:
    if i != spam[-1]:
        print( i + ', ', end = '')
    else:
        print('and '+ i)

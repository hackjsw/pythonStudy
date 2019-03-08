while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('Hello,joe.What is the password?(it is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

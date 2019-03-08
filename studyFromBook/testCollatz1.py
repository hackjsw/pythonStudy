def collatz(n):
    if n%2 == 0:
        print(n // 2)
        return n // 2
    elif n%2 == 1:
        print(3*n + 1)
        return 3*n + 1
    
print('Enter a number: ')
shu=int(input())
while shu != 1:
    shu=collatz(shu)

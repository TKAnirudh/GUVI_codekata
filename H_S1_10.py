n = input()
x = set(map(int,input().split()))
y = set(map(int,input().split()))

if y.issubset(x):
    print('YES')
else:
    print('NO')


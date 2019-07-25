n = list(map(int,input().split()))
x = list(map(int,input().split()))
x = list(dict.fromkeys(x))
x.sort()
x.reverse()

print(x[n[1]-1])


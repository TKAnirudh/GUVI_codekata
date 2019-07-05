
x = int(input())

y = list(map(int,input().split()))
 
z =0
y.sort()

for i in range(x):

  z = z*10 + y[i]

print(z)

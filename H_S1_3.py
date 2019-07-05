x = int(input())

y = list(map(int,input().split()))
 
z = []


for i in range(x):

  if (i==y[i]):
    z.append(y[i])

z.sort()


for i in range(len(z)):
  print(z[i],end=' ')

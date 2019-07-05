x = int(input())

y = list(map(int,input().split()))
 
z = []


for i in range(x):
  for j in range(i+1,x):

    if (y[i]==y[j]):
      z.append(y[i])

a = set(y)-set(z)
b = list(a)


for i in range(len(b)):
  print(b[i],end=' ')

if (len(b)==0):
  print("-1")

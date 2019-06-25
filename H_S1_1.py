n = int(input())
x = list(map(int,input().split()))
y =[]
for i in range(n):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
          y.append(x[i])

if (len(y)==0):
    print("unique")
else:
    y.sort()
    y=set(y)
    for i in y:
        print(i,end=" ")

n = input()
x = list(map(int,input().split()))
o = []
e = []
for i in range(len(x)):

    if i%2 == 0:
        if x[i]%2 != 0:
            o.append(x[i])    
    else:
        if x[i]%2 == 0:
            o.append(x[i])


for i in range(len(o)):
    print(o[i],end=" ")
    

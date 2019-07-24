n = input()
x = list(map(int,input().split()))

for i in range (len(x)):
    for j in range (i+1,len(x)):

        for k in range (j+1,len(x)):
            l = []
            if x[i]+x[j] == x[k]:
                if x[i]<x[j]:
                    print(x[i],x[j],x[k])
            

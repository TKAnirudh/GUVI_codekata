n = input()
x = list(map(int,input().split()))

for i in range(len(x)):
    for j in range(i+1,len(x)):
        #print (x[i],x[j])
        if (i!=j) and (x[i]+x[j]==0):
            print (x[i],x[j])
            #continue



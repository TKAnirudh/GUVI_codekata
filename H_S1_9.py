n = input()
x = list(map(int,input().split()))
#x = list(dict.fromkeys(x))

def mod(n):
    if n<=0:
        return -n
    else:
        return n
y =[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        #print (x[i],x[j])
        if (i!=j) and ((x[i]+x[j]==0)):
            y.extend([x[i],x[j]])
            print(x[i],x[j])
            break
            
if len(y) == 0:
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            #print (x[i],x[j])
            if (i!=j) and ((mod(x[i]+x[j])==1)):
                print(x[i],x[j])
                break


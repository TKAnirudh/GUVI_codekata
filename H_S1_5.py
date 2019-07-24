def count(lis):
    a = 0
    for i in range (len(lis)-1):
        #print(int(x[i]+x[i+1]))
        if (10<=int(x[i]+x[i+1])<=26):
            a += 1
    #print('---')
    return a

x = list(input())

c = 0
s = 0
while (c<len(x)-1):
    #print(x[c:len(x)])
    x = x[c:len(x)]
    s += count(x)

    c += 2

print (s+1)


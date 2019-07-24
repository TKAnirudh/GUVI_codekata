n = input()
x = list(map(str,input().split()))
c = ''
for i in range(len(x)):

    if x[i] in x[i+1:len(x)]:

        c += x[i]
        break

if len(c)==0:
    print("unique")
else:
    print(c)


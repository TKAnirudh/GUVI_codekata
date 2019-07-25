n = input()
#x = set(map(int,input().split()))

x = n.split(' ')

for i in range(len(x)):
    print(x[i][::-1],end=" ")

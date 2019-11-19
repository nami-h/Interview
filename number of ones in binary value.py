def bit(k):
    
    for i in k:
        count=0
        for j in i:
            if j=='1':
                count+=1
        print(count)

T=int(input())
l=[]
for i in range(0, T):
    n=int(input())
    l.append(bin(n))
bit(l)

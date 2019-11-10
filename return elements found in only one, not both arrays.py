def uncommon(a1,a2):
    l=[]
    m=[]
    for i in a1:
        if i not in a2:
            l.append(i)
    for j in a2:
        if j not in a1:
            m.append(j)
    return l, m

a1=[-1,0,1,2,3,4,5,6,7,8,9,10]
a2=[7,8,9,10,11,12,13,14,15,16]
print(uncommon(a1, a2))

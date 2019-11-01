def rev(n):
    l=n.split(".")
    first=0
    last=len(l)-1
    while first<last:
        temp=l[first]
        l[first]=l[last]
        l[last]=temp
        first+=1
        last-=1
    return '.'.join(l)
    




n="I.like.programming.a.lot"
print(rev(n))

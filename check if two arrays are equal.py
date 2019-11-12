def rep(a, b):
    
    if len(a)!=len(b):
        return False
    a.sort()
    b.sort()
    
    for i in range(0, len(a)-1):
        if a[i]!=b[i]:
            return False
    return True
            


a=[1,2,3,99999,4,5,6,6]
b=[1,2,3,6,6,5,4,9999]
print(rep(a, b))

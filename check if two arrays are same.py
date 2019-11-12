def rep(a, b):
    
    if len(a)!=len(b):
        return False
    for i in a :
        if i in b:
            b.remove(i)
    if b==[]:
        return True



a=[1,2,3,4,5,6,6]
b=[1,2,3,6,6,5,4]
print(rep(a, b))

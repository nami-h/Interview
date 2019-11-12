def rep(a):
    dict={}
    for i in a:
        if i not in dict:
            dict[i]=1 
        else:
            dict[i]+=1
    print(dict)
    for i in a:
        if dict[i]==1:
            return i



a="missisippi"
print(rep(a))

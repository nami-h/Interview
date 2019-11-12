def wave_sort(a):
    
    a.sort()
    
    for i in range(0, len(a)-1, 2):
        a[i], a[i+1]=a[i+1],a[i]
    
    


a=[1,2,3,99999,4,5,6,6,.9,12,765]
wave_sort(a)
for i in range(0, len(a)):
    print(a[i])

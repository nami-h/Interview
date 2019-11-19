def insertion(arr):
    for i in range(1, len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and k<=arr[j]:
            arr[j+1]=arr[j]
            j-=1 
        arr[j+1]=k 

arr=[23,-7,9,12,4]
insertion(arr)
for i in range(len(arr)):
    print(arr[i])
        
        

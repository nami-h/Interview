def reverse_in_place(lst):     
    size = len(lst)             
    hiindex = size - 1
    its = int(size/2)           # Number of iterations required
    for i in range(0, its):     # i is the low index pointer
        temp = lst[hiindex]     # Perform a classic swap
        lst[hiindex] = lst[i]
        lst[i] = temp
        hiindex -= 1            # Decrement the high index pointer

array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]

print (array)                
reverse_in_place(array)         
print (array)                   

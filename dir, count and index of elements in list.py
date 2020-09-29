my_list=[]
print(type(my_list))
my_list=['whatever', 'hello', 23, 9.4]
print(my_list[-1])
my_list[2]='MYY NEW ELEMENT'
print(my_list)
print(len(my_list))
my_list.append('hello')
print(my_list)
my_list +=[2, 3.9, 'n']
print(my_list)
my_list.extend([9,'mill'])
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop(2)
print(my_list)
del(my_list[3])
print(my_list)
print(dir(my_list))
print(my_list.count('hello'))
print(my_list.index('hello'))   #first occurance
my_list.remove('hello')  #first occurance
print(my_list)

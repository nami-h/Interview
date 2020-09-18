def count(x):
    num=0
    while x:
        num+=x&1 
        x>>=1 
    return num   

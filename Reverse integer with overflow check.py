class Solution:
    def reverse(self, x: int) -> int: 
        sign=1
        if x<0:
            sign=-1
        num=0
        x=abs(x)
        while x>0:
            d=x%10
            x=x//10
            num=num*10+d
        if num>(2**31)-1:
            return 0
        return num*sign

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=0
        y=x
        while x>0:
            d=x%10
            x=x//10
            num=num*10+d
        if num==y:
            return True
        else:
            return False
        
        

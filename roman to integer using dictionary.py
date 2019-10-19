class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        roman={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I': 1}
        for i in range(0, len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                res-=roman[s[i]]
            else:
                res+=roman[s[i]]
        return res+roman[s[-1]]

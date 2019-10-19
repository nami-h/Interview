class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n=sorted(strs)
        for i in range (len(n[0])):
            for string in (n[1:]):
                if (string[i]!=n[0][i]) or (i>=len(string)):
                    return n[0][:i]
        return n[0]       
                

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = {}
        
        for c in s:
            if c in alphabet:
                alphabet[c] += 1
            else:
                alphabet[c] = 1
        
        for c in t:
            if c in alphabet:
                alphabet[c] -= 1
            else:
                return False
        
        for c in s:
            if alphabet[c] != 0:
                return False
        return True

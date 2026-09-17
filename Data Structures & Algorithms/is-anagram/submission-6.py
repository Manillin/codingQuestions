class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        b1 = [0] * 26 
        b2 = [0] * 26 

        for c in s:
            b1[ord(c) - ord('a')] += 1 
        for c in t:
            b2[ord(c) - ord('a')] += 1 
        
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                return False 
        return True
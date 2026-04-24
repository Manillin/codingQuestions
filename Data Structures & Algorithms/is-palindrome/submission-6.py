class Solution:

    def isAlNum(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or 
            ord('0') <= ord(s) <= ord('9'))
        


    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1 
        while l < r:
            while l < r and not self.isAlNum(s[l].lower()):
                l+=1
            
            while r > l and not self.isAlNum(s[r].lower()):
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True 




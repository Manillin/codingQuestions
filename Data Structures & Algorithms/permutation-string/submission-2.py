class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False  
        s1map = {}
        s2map = {}

        for s in 'abcdefghijklmnopqrstuvwxyz':
            s1map[s] = 0
            s2map[s] = 0

        for c in s1:
            s1map[c] += 1
        for i in range(len(s1)):
            s2map[s2[i]]+=1
        
        l=0
        for r in range(len(s1), len(s2), 1):
            if (s1map == s2map):
                return True 
            
            s2map[s2[l]]-=1
            s2map[s2[r]]+=1
            l+=1
        return True if s1map == s2map else False  






    
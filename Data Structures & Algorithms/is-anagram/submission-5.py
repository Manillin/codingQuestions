class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for c in s:
            map1[c] += map1[c] + 1 
        for c in t:
            map2[c] += map2[c] + 1
        
        return map1 == map2
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        countT = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            countT[c] += 1
        
        res = [-1,-1]
        resLen = float("infinity")
        l=0
        have = 0
        need = len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] += 1 
            if c in countT and window[c] == countT[c]:
                have += 1 
                while have == need: 
                    if r-l+1 < resLen:
                        res = [l,r]
                        resLen = r-l+1
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]: 
                        have-=1 
                    l+=1
        l,r = res 
        return s[l:r+1] if resLen != float("infinity") else ""

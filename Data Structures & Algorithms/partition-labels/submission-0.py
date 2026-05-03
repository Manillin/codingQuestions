class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i 
        
        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])

            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result  
            
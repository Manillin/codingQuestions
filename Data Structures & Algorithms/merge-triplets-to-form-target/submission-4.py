class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for t in triplets:
            if len(found) == 3:
                return True 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue 
            
            for i, n in enumerate(t):
                if n == target[i]:
                    found.add(i)
        return len(found) == 3

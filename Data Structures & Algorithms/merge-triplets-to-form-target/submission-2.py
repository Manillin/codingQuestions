class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        moves = set()

        for t in triplets:
            if len(moves) == 3:
                return True
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue 
            
            for i, num in enumerate(t):
                if num == target[i]:
                    moves.add(i)
        
        return len(moves) == 3 
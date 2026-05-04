class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        
        two = 1
        one = 2

        for i in range(3,n+1):
            current = one+two 
            two = one 
            one = current 
        return one 
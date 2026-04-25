class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = (ROWS * COLS) -1 
        while l<=r:
            mid = (l + r) // 2
            nr, nc = divmod(mid,COLS)

            if matrix[nr][nc] > target:
                r = mid -1 
            elif matrix[nr][nc] < target:
                l = mid +1
            else:
                return True 
        return False 
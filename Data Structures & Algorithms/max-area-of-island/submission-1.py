class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(grid, r, c):
            if(r < 0 or r >= ROWS or c <0 or c >= COLS or grid[r][c] == 0):
                return 0

            area = 1 
            grid[r][c] = 0
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                nr,nc = r+dr, c+dc
                area += dfs(grid, nr, nc)
            return area


        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(grid,r,c))
        return max_area 
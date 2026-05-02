class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def dfs(grid, r, c):
            if (r < 0 or r >= ROWS or c <0 or c >= COLS or grid[r][c] == '0'):
                return 
            grid[r][c] = '0'
            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(grid, nr, nc)
            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(grid, r,c)
                    islands+=1
        return islands

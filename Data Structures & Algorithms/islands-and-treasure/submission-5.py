class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= ROWS or nc <0 or nc>= COLS or grid[nr][nc] != INF:
                        continue 
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        q = deque()
        rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten+=1
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        while q:
            if fresh == 0:
                break
            time+=1
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if nr < 0 or nr >= ROWS or nc<0 or nc>=COLS or grid[nr][nc] != 1:
                        continue 
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh-=1
        return time if not fresh else -1 

        
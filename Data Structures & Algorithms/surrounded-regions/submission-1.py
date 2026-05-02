class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if board[r][c] != 'O':
                return 

            board[r][c] = 'S'
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in dirs:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
        
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[rows-1][c] == 'O':
                dfs(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'





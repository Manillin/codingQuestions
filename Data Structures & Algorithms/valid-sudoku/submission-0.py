class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        # check rows 

        for i in range(ROWS):
            row_set = set()
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])
        
        for i in range(COLS):
            col_set = set()
            for j in range(ROWS):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_set:
                    return False 
                else:
                    col_set.add(board[j][i])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
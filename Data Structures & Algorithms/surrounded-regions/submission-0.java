class Solution {
    private final int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public void solve(char[][] board) {
        if(board == null || board.length == 0 || board[0].length == 0){
            return;
        }
        int ROWS = board.length;
        int COLS = board[0].length;

        for(int c = 0; c < COLS; c++){
            if(board[0][c] == 'O'){
                dfs(board,0,c);
            }
            if(board[ROWS-1][c] == 'O'){
                dfs(board, ROWS-1, c);
            }
        }
        for(int r = 0; r < ROWS; r++){
            if(board[r][0] == 'O'){
                dfs(board, r, 0);
            }
            if(board[r][COLS-1] == 'O'){
                dfs(board, r, COLS-1);
            }
        }

        for(int r = 0; r<ROWS; r++){
            for(int c = 0; c< COLS;c++){
                if(board[r][c] == 'O'){
                    board[r][c] = 'X';
                }else if(board[r][c] == 'T'){
                    board[r][c] = 'O';
                }
            }
        }
    }

    private void dfs(char[][] board, int r, int c){
        if(r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != 'O'){
            return;
        }
        board[r][c] = 'T';
        for(int[]dir: directions){
            int nr = r+dir[0];
            int nc = c + dir[1];
            dfs(board, nr,nc);
        }
    }
}

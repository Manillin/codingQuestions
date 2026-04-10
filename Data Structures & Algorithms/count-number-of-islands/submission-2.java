class Solution {

    private int dfs(char[][]grid,int i,int j,int R,int C){
        if( i < 0 || i >= R || j < 0 || j >= C ||grid[i][j] == '0'){
            return 0;
        }
        grid[i][j] = '0';
        dfs(grid,i+1,j,R,C);
        dfs(grid,i-1,j,R,C);
        dfs(grid,i,j+1,R,C);
        dfs(grid,i,j-1,R,C);
        return 1;
    }

    public int numIslands(char[][] grid) {
        
        int islands = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;
        for(int i=0;i<ROWS;i++){
            for(int j=0; j< COLS;j++){
                islands += dfs(grid,i,j,ROWS,COLS);
            }
        }
        return islands;
    }
}

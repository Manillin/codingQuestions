class Solution {

private static final int[][] dirs = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
    
    private void dfs(char[][]grid,int i,int j){
        if( i < 0  || j < 0 || i >= grid.length || j>= grid[0].length ||grid[i][j] == '0'){
            return;
        }
        grid[i][j] = '0';

        for(int[]dir: dirs){
            dfs(grid, i+dir[0], j+dir[1]);
        }
    }

    public int numIslands(char[][] grid) {
        int islands = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;
        for(int i=0;i<ROWS;i++){
            for(int j=0; j< COLS;j++){
                if(grid[i][j] == '1'){
                    dfs(grid,i,j);
                    islands++;
                }
            }
        }
        return islands;
    }
}

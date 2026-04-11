class Solution {

    private static final int[][] directions = {{1,0},{-1,0}, {0,1}, {0,-1}};
    private int dfs(int[][]grid,int r,int c){
        if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0){
            return 0;
        }
        grid[r][c] = 0;
        int area = 1;
        for(int[] dir: directions){
            area += dfs(grid, r+dir[0], c +dir[1]);
        }
        return area;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;


        for(int r=0; r<ROWS;r++){
            for(int c=0; c<COLS;c++){
                if(grid[r][c] == 1){
                    max_area = Math.max(max_area, dfs(grid,r,c));
                }
            }
        }
        return max_area;
    }
}

class Solution {
    private final int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int ROWS = heights.length;
        int COLS = heights[0].length;
        List<List<Integer>> result = new ArrayList<>();

        boolean[][] pacific = new boolean[ROWS][COLS];
        boolean[][] atlantic = new boolean[ROWS][COLS];

        for(int c = 0;c<COLS;c++){
            dfs(0, c, pacific, heights);
            dfs(ROWS-1, c, atlantic, heights);

        }
        for(int r=0; r<ROWS;r++){
            dfs(r, 0 , pacific, heights);
            dfs(r, COLS-1, atlantic, heights);
        }
        for(int r=0;r<ROWS;r++){
            for(int c=0;c<COLS;c++){
                if(pacific[r][c] && atlantic[r][c]){
                    result.add(Arrays.asList(r,c));
                }
            }
        }
        return result;
    }

    private void dfs(int r, int c, boolean[][] visited, int[][]heights){
        if(visited[r][c]){
            return;
        }
        visited[r][c] = true;
        for(int i=0; i<directions.length;i++){
            int nr = r + directions[i][0];
            int nc = c + directions[i][1];
            if(nr < 0 || nr >= heights.length || nc < 0 || nc >= heights[0].length || visited[nr][nc]){
                continue;
            }
            if(heights[nr][nc] < heights[r][c]){
                continue;
            }
            dfs(nr,nc,visited,heights);
        }
    }
}

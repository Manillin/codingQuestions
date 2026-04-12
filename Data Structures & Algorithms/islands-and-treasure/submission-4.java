class Solution {
    private static final int[][] directions = new int[][]{{0,1}, {0,-1}, {1,0},{-1,0}};
    public void islandsAndTreasure(int[][] grid) {
        Deque<int[]> q = new ArrayDeque<>();
        int ROWS = grid.length;
        int COLS = grid[0].length;
        for(int r=0;r<ROWS;r++){
            for(int c=0;c<COLS;c++){
                if(grid[r][c] == 0){
                    q.add(new int[]{r,c});
                }
            }
        }
        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0;i<len;i++){
                int[] cord = q.poll();
                for(int[] dir: directions){
                    int nr = cord[0]+dir[0];
                    int nc = cord[1]+dir[1];
                    if(nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS || grid[nr][nc]!=2147483647){
                        continue;
                    }else{
                        grid[nr][nc] = grid[cord[0]][cord[1]] + 1;
                        q.add(new int[]{nr,nc});
                    }
                }

            }
        }
    }
}

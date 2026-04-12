class Solution {
    private static final int[][] directions = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
    public int orangesRotting(int[][] grid) {
        Deque<int[]> q = new ArrayDeque<>();
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int minutes=0;
        int fresh=0;
        for(int r=0;r<ROWS;r++){
            for(int c=0;c<COLS;c++){
                if(grid[r][c] == 2){
                    q.add(new int[]{r,c});
                }else if(grid[r][c] == 1){
                    fresh++;
                }
            }
        }

        while(!q.isEmpty() && fresh > 0){
            int len = q.size();
            boolean incr_minutes = false;
            for(int i=0;i<len;i++){
                int[] cords = q.poll();
                int r = cords[0];
                int c = cords[1];
                for(int[] dir:directions){
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if(nr < 0 || nr >= ROWS || nc <0 || nc >= COLS || grid[nr][nc]!=1){
                        continue;
                    }else{
                        incr_minutes = true;
                        q.add(new int[]{nr,nc});
                        grid[nr][nc] = 2;
                        fresh--;
                    }
                }
            }
                if(incr_minutes == true){
                        minutes++;
            }
        }
        return fresh == 0? minutes:-1;        
    }
}

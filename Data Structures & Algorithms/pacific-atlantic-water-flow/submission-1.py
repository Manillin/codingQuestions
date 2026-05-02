class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c , visited, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            
            if (r,c) in visited or heights[r][c] < prev_height:
                return 

            visited.add((r,c))

            dirs = [[1,0], [-1,0], [0,-1], [0,1]]

            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                dfs(nr, nc, visited, heights[r][c])
        
        result = []

        # dfs form pacific borders
        for c in range(cols):
            dfs(0,c,pacific, heights[0][c])
        for r in range(rows):
            dfs(r,0, pacific, heights[r][0])
        
        # dfs from atlantic borders
        for c in range(cols):
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r, cols-1, atlantic, heights[r][cols-1])


        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result 




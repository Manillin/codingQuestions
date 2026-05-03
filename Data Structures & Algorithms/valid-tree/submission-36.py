class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False 
        
        graph = {i:[] for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False 
            visited.add(node)

            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False 
            return True 
        dfs(0,-1)
        return len(visited) == n
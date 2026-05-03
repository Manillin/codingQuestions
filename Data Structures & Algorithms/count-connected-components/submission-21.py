class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue 
                dfs(nei)
        ccomp = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                ccomp+=1

        return ccomp
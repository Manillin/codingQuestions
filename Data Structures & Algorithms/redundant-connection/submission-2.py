class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) +1 )]
        rank = [1] * (len(edges) +1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False 
            
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b 
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            return True 
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []
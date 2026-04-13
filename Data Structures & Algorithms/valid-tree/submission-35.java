class Solution {
    public boolean validTree(int n, int[][] edges) {
        if(edges.length != n-1){
            return false;
        }
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0; i<n;i++){
            graph.add(new ArrayList<>());
        }
        for(int[] edge: edges){
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        boolean[] visited = new boolean[n];
        dfs(0, graph, visited);
        for(boolean nodeVisited: visited){
            if(!nodeVisited){
                return false;
            }
        }
        return true;

    }

    private void dfs(int node, List<List<Integer>> graph, boolean[] visited){
        // skip said node if already visited 
        if(visited[node]){
            return;
        }

        visited[node] = true;
        for(int nei: graph.get(node)){
            dfs(nei, graph, visited);
        }
    }
}

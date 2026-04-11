/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    private Node dfs(Node node, Map<Node,Node> map){
        if(map.containsKey(node)){
            return map.get(node);
        }
        Node new_node = new Node(node.val);
        map.put(node, new_node);
        for(Node neigh: node.neighbors){
            new_node.neighbors.add(dfs(neigh, map));
        }
        return new_node;
    }

    public Node cloneGraph(Node node) {
        if(node == null){
            return node;
        }
        Map<Node,Node> map = new HashMap<>();
        return dfs(node,map);
    }
}








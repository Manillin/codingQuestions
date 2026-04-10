/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public void dfs(TreeNode root, List<Integer> res){
        if(root == null){
            return;
        }
        dfs(root.left, res);
        res.add(root.val);
        dfs(root.right, res);
    }

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> order = new ArrayList<>();
        dfs(root, order);
        return order.get(k-1);
    }
}

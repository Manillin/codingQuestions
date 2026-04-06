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
    boolean balanced = true;
    public int heigth(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = heigth(root.left);
        int right = heigth(root.right);
        if(Math.abs(left-right) > 1){
            balanced = false;
        }
        return Math.max(left, right) +1;
    }

    public boolean isBalanced(TreeNode root) {
        if(root == null){
            return true;
        }
        int left =heigth(root.left);
        int right= heigth(root.right);
        if(Math.abs(left-right) > 1){
            balanced = false;
        }
        return balanced;
    }
}

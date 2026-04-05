class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while(l <= r){
            int mid = (l + r) / 2; 
            if(nums[mid] > target){
                r--;
            }else if(nums[mid] < target){
                l++;
            }else{
                return mid;
            }
        }
        return -1;
    }
}
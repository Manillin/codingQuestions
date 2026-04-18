class Solution {
    public int maxArea(int[] heights) {
        if(heights.length <= 0){
            return 0;
        }
        int l = 0;
        int r = heights.length-1;
        int maxArea = 0;
        while(l<r){
            int base = r - l;
            int height = Math.min(heights[l], heights[r]);
            maxArea = Math.max(maxArea, base*height);
            if(heights[r] > heights[l]){
                l++;
            }else{
                r--;
            }
        }
        return maxArea;
    }
}

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int r = Arrays.stream(piles).max().getAsInt();
        int l = 1;
        int res=r;
        while(l<=r){
            int k = (l+r) / 2;
            int totalTime = 0;
            for(int pile: piles){
                totalTime += Math.ceil((double)pile / k);
            }
            if(totalTime <= h){
                res = k;
                r = k- 1;
            }else{
                l = k +1;
            }
        }
        return res;
    }
}
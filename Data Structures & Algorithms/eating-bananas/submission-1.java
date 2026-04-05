class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = Arrays.stream(piles).max().getAsInt();
        
        int result=r;
        while(l <= r){
            int eatingSpeed = (l+r) / 2;
            int hours = 0;
            for(int pile: piles){
                hours += Math.ceil((double)pile/eatingSpeed);
            }
            if(hours > h){
                l = eatingSpeed + 1;
            }else if(hours <= h){
                result = eatingSpeed;
                r = eatingSpeed - 1;
            }
        }
        return result;
    }
}

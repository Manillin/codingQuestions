class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set = Arrays.stream(nums)
                            .boxed()
                            .collect(Collectors.toSet());
        int res = 0;
        for(int num: num_set){
            if(num_set.contains(num - 1) == false){
                int len = 0;
                while(num_set.contains(num+len)){
                    len+=1;
                }
                res = Math.max(len, res);
            }
        }
        return res;
    }
}
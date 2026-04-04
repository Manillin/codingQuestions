class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] bucket = new List[n];
        for(int i=0; i<n;i++){
            bucket[i] = new ArrayList<>();
        }
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0) +1);
        }
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            bucket[entry.getValue()-1].add(entry.getKey());
        }
        
        int[] res = new int[k];
        int index = 0;
        for(int i=n-1; i>-1;i--){
            for(int num: bucket[i]){
                res[index] = num;
                index++;
                if(index == k){
                    return res;
                }
            }
        }
        return res;
    }
}
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for(char task: tasks){
            freq[task-'A']++;
        }
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> b-a);
        for(int count: freq){
            if(count>0){
                maxHeap.offer(count);
            }
        }
        
        int time = 0;
        while(!maxHeap.isEmpty()){
            List<Integer> remaining = new ArrayList<>();
            int slotsUsed = 0;

            for(int i=0; i<=n;i++){
                if(!maxHeap.isEmpty()){
                    int count = maxHeap.poll();
                    count--;
                    slotsUsed++;

                    if(count > 0 ){
                        remaining.add(count);
                    }
                }
            }

            for(int count: remaining){
                maxHeap.offer(count);
            }
            if(maxHeap.isEmpty()){
                time+=slotsUsed;
            }else{
                time+= n+1;
            }
        }
        return time;
    }
}


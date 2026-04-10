class KthLargest {
    private PriorityQueue<Integer> heap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.heap = new PriorityQueue<>();
        this.k = k;
        for(int num: nums){
            heap.offer(num);
            if(heap.size() > k){
                heap.poll();
            }
        }
    }
    
    public int add(int val) {
        heap.add(val);
        if(heap.size() > k){
            heap.poll();
        }
        return heap.peek();
    }
}

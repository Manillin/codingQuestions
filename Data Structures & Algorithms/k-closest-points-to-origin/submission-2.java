class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a,b) -> Integer.compare(b[0], a[0])
        );

        for(int i=0; i<points.length;i++){
            int dist = (points[i][0] * points[i][0]) + (points[i][1]*points[i][1]);
            heap.offer(new int[]{dist, points[i][0], points[i][1]});
            if(heap.size() > k){
                heap.poll();
            }
        }

        int[][] result = new int[k][2];
        int i= 0;
        while(!heap.isEmpty()){
            int[] val = heap.poll();
            result[i] = new int[]{val[1], val[2]};
            i++;
        }
        return result;
    }
}

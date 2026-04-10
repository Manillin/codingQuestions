class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<double[]> heap = new PriorityQueue<>(
            (a,b) -> Double.compare(a[0],b[0])
        );
        for(int i=0; i<points.length;i++){
            double dist = Math.sqrt( (points[i][0] * points[i][0]) + (points[i][1]*points[i][1]) );
            heap.offer(new double[]{dist, points[i][0], points[i][1]});
        }
        int[][] result = new int[k][2];
        for(int i=0; i<k;i++){
            double[] values = heap.poll();
            int x = (int)values[1];
            int y = (int)values[2];
            result[i] = new int[]{x,y};
        }
        return result;
    }
}

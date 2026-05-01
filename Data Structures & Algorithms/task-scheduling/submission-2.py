class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        heap = [-task for task in count.values()]
        heapq.heapify(heap)
        q = deque()

        while q or heap:
            time+=1

            if heap:
                element = 1 + heapq.heappop(heap)
                if element:
                    q.append([element, time + n])
            
            else:
                time = q[0][1]
            
            if q and q[0][1] <= time:
                heapq.heappush(heap, q.popleft()[0])
        return time 
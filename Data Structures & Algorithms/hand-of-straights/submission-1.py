class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        count = defaultdict(int)
        for card in hand:
            count[card] += 1 
        
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            for card in range(start, start+groupSize):
                if card not in count or count[card] == 0:
                    return False 
                count[card]-=1 

                if count[card] == 0:

                    heapq.heappop(min_heap)
        return True 
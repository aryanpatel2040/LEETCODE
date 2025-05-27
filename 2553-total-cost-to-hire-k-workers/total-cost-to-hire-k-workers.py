class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        i, j = 0, len(costs) - 1
        start_heap, end_heap = [], []
        for _ in range(k):
            while len(start_heap) < candidates and i <= j:
                heapq.heappush(start_heap, costs[i])
                i += 1
            while len(end_heap) < candidates and i <= j:
                heapq.heappush(end_heap, costs[j])
                j -= 1

            if start_heap and end_heap:
                if start_heap[0] <= end_heap[0]:
                    res += heapq.heappop(start_heap)
                else:
                    res += heapq.heappop(end_heap)
            elif start_heap:
                res += heapq.heappop(start_heap)
            else:
                res += heapq.heappop(end_heap)
            
        return res
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, freq in count_nums.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        return [val for _, val in heap]
        
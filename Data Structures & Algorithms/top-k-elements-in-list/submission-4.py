import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = Counter(nums)
        heap = []
        for num, freq in count_nums.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for _, val in heap]
        
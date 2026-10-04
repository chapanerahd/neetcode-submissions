import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = dict()
        for num in nums:
            count_nums[num] = 1 + count_nums.get(num, 0)

        min_heap = list()
        for num, count in count_nums.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        ans = [num for count, num in min_heap]
        return ans

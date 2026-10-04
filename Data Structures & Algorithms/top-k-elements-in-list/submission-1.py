import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = dict()
        for num in nums:
            count_nums[num] = 1 + count_nums.get(num, 0)

        data = list()
        for val in count_nums.values():
            if len(data) < k:
                heapq.heappush(data, val)
            else:
                heapq.heappushpop(data, val)
                
        ans = list()
        for num, count in count_nums.items():
            if count >= data[0]:
                ans.append(num)
        return ans        
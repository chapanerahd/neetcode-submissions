from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = Counter(nums)
        unique_frequncies = list(count_nums.values())
        heapq.heapify(unique_frequncies)

        for i in range(len(count_nums) - k):
            heapq.heappop(unique_frequncies)

        ans = []
        for num, count in count_nums.items():
            if count >= unique_frequncies[0]:
                ans.append(num)
        return ans        
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        freq_bucket = [[] for _ in range(len(nums) + 1)]  
        for num, freq in count_nums.items():
            freq_bucket[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        return res
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapper = dict()
        for i, num in enumerate(nums):
            if num in mapper:
                return [mapper[num], i]
            mapper[target - num] = i
        
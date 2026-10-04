class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapper = dict()
        for idx, num in enumerate(nums):
            if num in mapper:
                return [mapper[num], idx]
            
            mapper[target - num] = idx

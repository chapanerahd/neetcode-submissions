class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = set()
        for num in nums:
            if num in mapper:
                return True
            mapper.add(num)
        return False
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):

            # if i >=0 and nums[i] == nums[i-1]:
            #     continue
            # [-4,-1, -1, 0, 1, 2]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j +=1
        return list(res)

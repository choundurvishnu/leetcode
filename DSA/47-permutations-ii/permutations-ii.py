class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def helper(i):
            #base Condition
            if i == len(nums)-1:
                result.append(nums[:])
                return
            
            hash = {}
            for j in range(i,len(nums)):
                if nums[j] not in hash:
                    hash[nums[j]] = True
                    nums[i],nums[j] = nums[j],nums[i]
                    helper(i+1)
                    nums[i],nums[j] = nums[j],nums[i]

        helper(0)
        return result
        
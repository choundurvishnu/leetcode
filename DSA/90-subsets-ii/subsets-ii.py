class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def helper(i,curr):
            if i == len(nums):
                result.append(curr[:])
                return
            # include
            curr.append(nums[i])
            helper(i+1,curr)
            curr.pop()

            # Exclude
            while i < len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            helper(i+1,curr)
        helper(0,[])
        return result
        
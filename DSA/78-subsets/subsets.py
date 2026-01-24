class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(nums,i,subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            helper(nums,i+1,subset)
            subset.append(nums[i])
            helper(nums,i+1,subset)
            subset.pop()
        helper(nums,0,[])
        return result
        
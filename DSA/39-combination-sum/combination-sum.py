class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def helper(start,curr,curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(curr[:])
                return
            
            for j in range(start,n):
                curr.append(candidates[j])
                helper(j,curr,curr_sum+candidates[j])
                curr.pop()

        helper(0,[],0)
        return result
        
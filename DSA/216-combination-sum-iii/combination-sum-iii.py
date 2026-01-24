class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def helper(index, curr,curr_sum):
            if curr_sum == n and len(curr)==k:
                result.append(curr[:])
                return
            if curr_sum > n or len(curr)==k:
                return
            
            for j in range(index,10):
                curr.append(j)
                helper(j+1,curr,curr_sum+j)
                curr.pop()
        helper(1,[],0)
        return result
        
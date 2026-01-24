class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        n=len(candidates)
        def helper(index, curr,curr_sum):
            if curr_sum == target:
                result.append(curr[:])
                return
            if curr_sum > target:
                return
            if index > n-1:
                return
            
            hash = {}
            for j in range(index,n):
                if candidates[j] not in hash:
                    hash[candidates[j]] = True
                    curr.append(candidates[j])
                    helper(j+1,curr,curr_sum+candidates[j])
                    curr.pop()

        helper(0,[],0)
        return result
        
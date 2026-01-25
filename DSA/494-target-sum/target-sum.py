class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (target+total)%2 != 0:
            return 0
        
        P = (target+total)//2
        dp = [0]*(P+1)
        dp[0] = 1
        for num in nums:
            for s in range(P,num-1,-1):
                dp[s]+=dp[s-num]
        
        return dp[P]
        
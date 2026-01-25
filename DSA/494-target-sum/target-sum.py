class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        summ = sum(nums)
        dp = [[None]*(2*summ+1) for _ in range(n)]

        def helper(index, sum_nums):

            if index < 0:
                if sum_nums == target:
                    return 1
                else:
                    return 0
            if dp[index][sum_nums+summ]!= None:
                return dp[index][sum_nums+summ]
            neg = helper(index-1,sum_nums+-1*nums[index])
            pos = helper(index-1,sum_nums+nums[index]) 
            dp[index][sum_nums+summ] = neg + pos
            return dp[index][sum_nums+summ]
        return helper(n-1,0)




        """
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
        """
        
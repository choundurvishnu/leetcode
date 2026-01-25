class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_num = sum(nums)
        if sum_num%2!= 0 :
            return False
        target = sum_num//2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target]




        """
        n = len(nums)
        sum_num = sum(nums)
        if sum_num%2!= 0 :
            return False
        target = sum_num//2
        prev = [False]*(target+1)
        curr = [False]*(target+1)
        prev[0] = True
        curr[0] = True

        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1] <= j:
                    curr[j] = prev[j] or prev[j-nums[i-1]]
                else:
                    curr[j] = prev[j]
            prev = curr[:]
        return curr[target] 
        """      
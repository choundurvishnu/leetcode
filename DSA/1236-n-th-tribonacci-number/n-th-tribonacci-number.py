class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+2)
        if n>0:
            dp[1] = 1
            dp[2] = 1
        count = 2
        while(count <n):
            count+=1
            dp[count] = dp[count-1]+dp[count-2]+dp[count-3]
        return dp[n]
        
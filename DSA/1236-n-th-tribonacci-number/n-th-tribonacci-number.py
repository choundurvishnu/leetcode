class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        
        if n==1 or n==2:
            return 1
        
        a,b,c = 0,1,1
        for _ in range(3,n+1):
            a,b,c = b,c,a+b+c
        return c

        """
        dp = [0]*(n+2)
        if n>0:
            dp[1] = 1
            dp[2] = 1
        count = 2
        while(count <n):
            count+=1
            dp[count] = dp[count-1]+dp[count-2]+dp[count-3]
        return dp[n]
        """
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        def helper(i,j):
            if i==j:
                dp[i][j] = True
                return dp[i][j]
            if dp[i][j]!= -1:
                return dp[i][j]
            helper(i+1,j)
            helper(i,j-1)
            if s[i]==s[j] and (j==i+1 or helper(i+1,j-1)):
                dp[i][j] = True
            else:
                dp[i][j] = False

        helper(0,n-1)
        res = 0
        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if dp[i][j]:
                    res +=1
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        longest = s[0]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                    dp[i][j]=True
                else:
                    dp[i][j]=False
                if dp[i][j]:
                    longest = s[i:j+1]    



        return longest
        
        
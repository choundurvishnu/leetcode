class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if i==j:
                    dp[i][j] = True
                elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                    dp[i][j]=True
                else:
                    dp[i][j] =False

        res = []
        def helper(index,curr):
            if index > n-1:
                res.append(curr[:])
                return
            
            for i in range(index,n):
                if(dp[index][i]):
                    curr.append(s[index:i+1])
                    helper(i+1,curr)
                    curr.pop()



        helper(0,[])
        return res
        
        
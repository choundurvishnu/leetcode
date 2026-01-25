class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # space Optimization
        n = len(text1)
        m = len(text2)
        prev = [0]*(m+1)
        curr = [0]*(m+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr[:]
        return curr[m]



        """
        # Tabulation
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        """
        




        """
        n = len(text1)
        m = len(text2)
        dp = [[-1]*(m) for _ in range(n)]
        def helper(index1, index2):
            if index1 > n-1 or index2 > m-1:
                return 0
            if dp[index1][index2]!=-1:
                return dp[index1][index2]
            
            if text1[index1] == text2[index2]:
                dp[index1][index2]= 1+helper(index1+1,index2+1)
            else:
                dp[index1][index2] =  max(helper(index1,index2+1),helper(index1+1,index2))
            return dp[index1][index2]
        return helper(0,0)
        """


        """
        n = len(text1)
        m = len(text2)
        def helper(index1, index2):
            if index1 > n-1 or index2 > m-1:
                return 0
            
            if text1[index1] == text2[index2]:
                return 1+helper(index1+1,index2+1)
            return max(helper(index1,index2+1),helper(index1+1,index2))
        

        return helper(0,0)
        """
    
        
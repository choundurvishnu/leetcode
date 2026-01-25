class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        #----- Tabulation-------
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(n+1):
            dp[i][0] = i
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    replace = 1 + dp[i-1][j-1]
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    dp[i][j] = min(replace,insert,delete)
        return dp[n][m]


        """
        #---- Memorization----
        n = len(word1)
        m = len(word2)
        dp = [[-1]*m for _ in range(n)]

        def helper(index1,index2):
            if index1 > n-1 and index2 > m-1:
                return 0
            if index1 > n-1:
                return m-index2
            if index2 > m-1:
                return n-index1
            if dp[index1][index2] !=-1:
                return dp[index1][index2]
            
            if word1[index1] == word2[index2]:
                dp[index1][index2]= helper(index1+1,index2+1)
            else:
                replace = 1 + helper(index1+1,index2+1)
                delete = 1 + helper(index1+1,index2)
                insert = 1 + helper(index1,index2+1)
                dp[index1][index2] = min(replace,delete,insert)
            return dp[index1][index2]
        return helper(0,0)
        """


        """
        #---- Recursion --------
        n = len(word1)
        m = len(word2)

        def helper(index1,index2):
            if index1 > n-1 and index2 > m-1:
                return 0
            if index1 > n-1:
                return m-index2
            if index2 > m-1:
                return n-index1
            
            if word1[index1] == word2[index2]:
                return helper(index1+1,index2+1)
            replace = 1 + helper(index1+1,index2+1)
            delete = 1 + helper(index1+1,index2)
            insert = 1 + helper(index1,index2+1)
            return min(replace,delete,insert)
        return helper(0,0)
        """
        
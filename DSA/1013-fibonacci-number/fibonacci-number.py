class Solution:
    def fib(self, n: int) -> int:
        """
        # ---- Space Optimized------
        if n<=1:
            return n
        prev = 0
        curr = 1
        counter = 1
        while counter < n:
            next = prev + curr
            counter += 1
            prev = curr
            curr = next
        return curr


        """
        #--------Tabulation / Botton Up--------
        dp = [0]*(n+1)

        if n>0:
            dp[1] = 1
        
        count = 1
        while(count<n):
            count+=1
            dp[count] = dp[count-1]+dp[count-2]
        return dp[n]
        """
        """



        """
        #----- Memorization--------
        def fib1(n, ht={0:0,1:1}):
            if n in ht:
                return ht[n]
            else:
                ht[n] = fib1(n-1,ht)+fib1(n-2,ht)
                return ht[n]
        res = fib1(n)
        return res
        """






        """
        #-----Recursive------
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        """
        
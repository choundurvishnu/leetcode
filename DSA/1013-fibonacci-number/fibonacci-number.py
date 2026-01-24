class Solution:
    def fib(self, n: int) -> int:




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
        #-----Recursive------
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        """
        
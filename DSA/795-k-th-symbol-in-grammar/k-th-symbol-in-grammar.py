class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        len = 2**(n-1)
        mid = len//2
        if k <= mid:
            return self.kthGrammar(n-1,k)
        else:
            return int(not self.kthGrammar(n-1,k-mid))
        
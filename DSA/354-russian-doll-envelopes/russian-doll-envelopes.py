class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key = lambda x:(x[0],-x[1]))
        n = len(envelopes)
        sub = [envelopes[0][1]]

        def binary_search(sub,num):
            l,r = 0,len(sub)
            while l< r:
                mid = (l+r)//2
                if num>sub[mid]:
                    l = mid+1
                else:
                    r = mid
            return l
        
        for i in range(1,n):
            num = envelopes[i][1]
            if num > sub[-1]:
                sub.append(num)
            else:
                x = binary_search(sub,num)
                sub[x] = num
        return len(sub)


        """

        envelopes.sort(key = lambda x:(x[0],-x[1]))
        n = len(envelopes)
        dp = [1]*n
        maximum = 1

        for i in range(1,n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
            if dp[i]> maximum:
                maximum = dp[i]
        return maximum
        """


        
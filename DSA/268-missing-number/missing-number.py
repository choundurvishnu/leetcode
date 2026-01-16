class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor_sum =0
        for i in range(n+1):
            xor_sum ^= i
        
        for i in nums:
            xor_sum ^= i
        
        return xor_sum
        
        
        
        
        
        
        
        
        
        """      
                n = len(nums)
                total_expect = n*(n+1)/2
                total_actual = sum(nums)
                return int(total_expect-total_actual)
                
        """


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # Method 3:
        survivor = 0
        for i in range(2,n+1):
            survivor = (survivor+k)%i


        return survivor +1


        


        
        
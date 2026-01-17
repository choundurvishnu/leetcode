class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # Method 3:
        survivor = 0
        for i in range(2,n+1):
            survivor = (survivor+k)%i
        return survivor +1


        # Method 2 Intuition
        def josephus(n):
            if n==1:
                return 0
            return (josephus(n-1)+k)%n

        return josephus(n)+1


        
# Method 1
        arr = [i+1 for i in range(n)]

        def helper(arr, start_index):
            if len(arr)==1:
                return arr[0]
            
            index_to_remove = (start_index+k-1)%len(arr)
            del arr[index_to_remove]
            return helper(arr,index_to_remove)
            
        
        return helper(arr,0)


        
        
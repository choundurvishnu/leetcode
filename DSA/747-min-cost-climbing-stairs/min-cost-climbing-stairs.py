class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """
        """
        #-----Memorization Approach------
        n = len(cost)
        mincost = [-1]*n

        def helper(index):
            if index > n-1:
                return 0
            
            if mincost[index]!=-1:
                return mincost[index]
            
            onestep = cost[index]+helper(index+1)
            twostep = cost[index] + helper(index+2)
            mincost[index] = min(onestep,twostep)
            return mincost[index]
        return min(helper(0),helper(1))
        


        """
        #---- Recursive----------
        n = len(cost)
        def helper(index):
            if index > n-1:
                return 0
            
            onestep = cost[index] + helper(index+1)

            twostep = cost[index] + helper(index+2)
            return min(onestep,twostep)
        return min(helper(0),helper(1))
        """





        
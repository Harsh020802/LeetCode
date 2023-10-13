class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)

        '''
        while(p<k):
            if(cost[i]<=cost[i+1]):
                c+=cost[i]
                i+=2
            else:
                c+=cost[i+1]
                i+=2
            p=i
        return c
            '''
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])

        return min(cost[0],cost[1])
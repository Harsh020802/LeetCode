class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=1
        t=1
        for i  in range (0,n-1):
            temp=f
            f += t
            t=temp
        return f
        
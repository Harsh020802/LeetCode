import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = math.sqrt(x)
        m=math.floor(n)
        if(m<0):
            return int(m+1)
        else:
            return int(m)
        
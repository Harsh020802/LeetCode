class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c=0
        if(n==0):
            return False
        while(c==0):
            if(n==1):
                return True
            else:
                c=n%3
                n=n/3
        return False
        
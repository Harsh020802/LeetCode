class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        new=s.split()
        k=new[-1]
        for i in k:
            c+=1
        return c
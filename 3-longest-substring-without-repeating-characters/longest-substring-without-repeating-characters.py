class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[]
        if len(s) == 0:
            return 0
        for i in range(0,len(s)):
            res = []
            for j in range(i,len(s)):
                if(s[j] not in res):
                    res.append(s[j])
                else:
                    break
            a.append(len(res))
        return max(a)


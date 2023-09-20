class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''
        for c in s.lower():
            if c.isalnum():
                s1 += c
        print(s1)

        s = s1[::-1]
        return s1==s 
        
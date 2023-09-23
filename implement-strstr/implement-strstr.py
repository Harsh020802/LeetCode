class Solution(object):
    def strStr(self, haystack, needle):
         if haystack == needle:
            return 0
         if len(needle) == 0:
            return 0
         for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
         return -1
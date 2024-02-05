class Solution(object):
    def firstUniqChar(self, s):
        l=[]
        for i in range(0,len(s)):
            if s[i] not in s[i+1:] and s[i] not in l:
                return i
            else:
                l.append(s[i])
        return -1
            
        
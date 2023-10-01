class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        news=""
        for i in s:
            if i.isspace()==False:
                arr.append(i)
            else:
                while arr:
                    news += arr.pop()
                news+=" "
        while arr:
             news+=arr.pop()
        return news 


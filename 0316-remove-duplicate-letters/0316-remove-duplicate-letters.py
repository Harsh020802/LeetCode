class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            while stack and char < stack[-1] and stack[-1] in s[i:] and char not in seen:
                seen.remove(stack.pop())
            if char not in seen:
                seen.add(char)
                stack.append(char)
        
        return ''.join(stack)

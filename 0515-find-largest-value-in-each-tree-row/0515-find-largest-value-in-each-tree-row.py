class Solution(object):
    def largestValues(self, root):
        queue = deque()
        ans = []
        queue.append(root)
        if not root:
            return ans
        while queue:
            level = len(queue)
            max_val = float('-inf')
            for i in range(level):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                max_val = max(max_val, temp.val)
            ans.append(max_val)
        return ans
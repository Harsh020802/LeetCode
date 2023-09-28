# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def bstcreator(self,nums,start,end):
        if(start>end):
            return None
        mid=int((start+end)/2)
        root =TreeNode(nums[mid])
        root.left=self.bstcreator(nums,start,mid-1)
        root.right=self.bstcreator(nums,mid+1,end)
        return root
        
        
    def sortedArrayToBST(self, nums):
        start=0
        end=len(nums)-1
        return self.bstcreator(nums,start,end)
        
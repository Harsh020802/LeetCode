# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        left,right=0,len(nums)-1
        while(left<right):
            if(nums[left]==nums[right]):
                left+=1
                right-=1
            else:
                return False
        return True
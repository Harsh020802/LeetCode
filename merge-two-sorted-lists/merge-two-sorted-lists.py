# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1:
            return l2
        if not l2:
            return l1
        optional=ListNode
        newh=optional
        while(l1 and l2):
            if l1.val<=l2.val:
                newh.next=l1
                l1=l1.next
            elif l1.val>=l2.val:
                newh.next=l2
                l2=l2.next
            newh=newh.next
        if l1:
            newh.next=l1
        elif l2:
            newh.next=l2
        return optional.next
        
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new=[]
        n=0
        c=0
        for i in range (0,len(nums)):
            if(nums[i]!=val):
                new.append(nums[i])
                c+=1
            else:
                continue
        for i in range(0,len(new)):
            nums[i]=new[i]
        return c
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k=0
        c=0
        for i in range (0,len(nums)):
            if(nums[i]==target):
                c=1
                return i
        if(c==0):
            for j in range(0,len(nums)):
                if(target>nums[j]):
                    k=j+1
        return k

                

       
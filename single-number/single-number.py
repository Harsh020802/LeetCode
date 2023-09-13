class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        for i in range (0,k):
            c=nums.count(nums[i])
            if(c==1):
                s=nums[i]
                break
        return s
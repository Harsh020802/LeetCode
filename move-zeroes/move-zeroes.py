class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=len(nums)
        for i in range (0,k):
            if(nums[i]==0):
                nums.remove(0)
                nums.append(0)
        return nums
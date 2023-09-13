class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        c = 1
        k = len(nums)
        
        for i in range(1, k):
            if nums[i] != nums[i-1]:
                nums[c]=nums[i];
                c += 1
        
        return c

                
                
                
        
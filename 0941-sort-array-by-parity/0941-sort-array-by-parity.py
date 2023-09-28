import numpy as np
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        num=[]
        k=len(nums)
        for i in range (0,k):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        num=np.concatenate((even,odd))
        return num
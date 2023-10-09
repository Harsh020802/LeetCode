class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr=[]
        k=len(nums)
        for i in range (0,k):
            if(nums[i]==target):
                arr.append(i)
                break
        for j in range (k-1,-1,-1):
            if(nums[j]==target):
                arr.append(j)
                break
        if arr:
            return arr
        else:
            return [-1,-1]

        
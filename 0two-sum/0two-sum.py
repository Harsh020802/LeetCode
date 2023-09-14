class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        g=[]
        k=len(nums)
        for i in range (0,k):
            for j in range(i+1,k):
                if(nums[i]+nums[j]==target):
                    g.append(i)
                    g.append(j)
                    break;
        return g
        
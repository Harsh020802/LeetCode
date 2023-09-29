class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        greater=0
        less=0
        c=0
        k=len(nums)
        while(c<k-1):
            if(nums[c]==nums[c+1]):
                c+=1
            elif(nums[c]<nums[c+1]):
                greater=1
                break
            elif(nums[c]>nums[c+1]):
                less=1
                break
        if(greater==1):
            for i in range (0,k-1):
                if(nums[i]<=nums[i+1]):
                    continue
                else:
                    return False
        elif(less==1):
            for i in range (0,k-1):
                if(nums[i]>=nums[i+1]):
                    continue
                else:
                    return False
        return True

        
        
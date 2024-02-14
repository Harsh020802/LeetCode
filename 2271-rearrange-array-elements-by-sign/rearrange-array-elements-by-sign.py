class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        k=0
        p=[]
        n=[]
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i]>=0):
                p.append(nums[i])
            else:
                n.append(nums[i])
        for j in range(0,len(nums)):
            if(j%2==0):
                ans.append(p[k])
                k+=1
            else:
                ans.append(n[l])
                l+=1
        return ans
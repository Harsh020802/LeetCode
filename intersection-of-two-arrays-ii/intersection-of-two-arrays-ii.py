class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=[]
        if(len(nums1)<len(nums2)):
            k=nums1
            l=nums2
        else:
            l=nums1
            k=nums2
            
        for i in range(0,len(k)):
            if(k[i] in l ):
                s.append(k[i])
                l.remove(k[i])
                
                
        return s
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        min_common = float('inf')
        for i in nums1:
            if i in nums2:
                min_common = min(min_common, i)
        
        return min_common if min_common != float('inf') else -1
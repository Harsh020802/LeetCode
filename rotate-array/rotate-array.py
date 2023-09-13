class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
    
        # Reverse the entire array
        nums.reverse()
    
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
    
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
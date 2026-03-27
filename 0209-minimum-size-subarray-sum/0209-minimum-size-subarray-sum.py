class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0 
        window_sum = 0
        min_size = float('inf')
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                min_size = min(min_size, right-left+1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if min_size == float('inf') else min_size
        
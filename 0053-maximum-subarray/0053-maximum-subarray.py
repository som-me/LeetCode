class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs, maxs = nums[0],nums[0]
        for end in range(1, len(nums)):
            cs = max(nums[end], cs + nums[end])
            maxs = max(cs, maxs)
        return maxs
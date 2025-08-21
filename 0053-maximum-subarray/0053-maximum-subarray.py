class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs, maxs = 0, float('-inf')
        for end in nums:
            cs += end
            maxs = max(maxs, cs)
            if cs < 0:
                cs = 0
        return maxs

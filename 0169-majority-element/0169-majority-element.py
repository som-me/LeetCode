import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a, freq = 0, 0
        for i in range(len(nums)):
            if freq == 0:
                a = nums[i]
            if a == nums[i]:
                freq += 1
            else:
                freq -= 1
        return a

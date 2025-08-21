import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        floor = math.floor(n/2)
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for k, v in count.items():
            if v > floor:
                return k
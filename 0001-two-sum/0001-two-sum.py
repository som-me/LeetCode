class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in seen:
                return [seen[left], i]
            seen[num] = i

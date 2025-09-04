class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(numbers):
            left = target - num
            if left in seen:
                return [seen[left]+1, i+1]
            seen[num] = i
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        nums = list(map(lambda ch: roman[ch], s))
        total = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums [i] < nums [i+1]:
                total -= nums[i]
            else:
                total += nums[i]
        return total
        
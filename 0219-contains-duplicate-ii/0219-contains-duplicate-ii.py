class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}
        for i in range(len(nums)):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True
            last_index[nums[i]] = i
        return False

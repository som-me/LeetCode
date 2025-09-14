class Solution(object):
    def intersection(self, nums1, nums2):
        setA = set(nums1)
        setB = set(nums2)
        setC = list(setA.intersection(setB))
        return setC

        
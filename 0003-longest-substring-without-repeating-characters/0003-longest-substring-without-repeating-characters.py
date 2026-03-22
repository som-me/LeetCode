class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        char_str = set()
        left = 0
        max_len = 0

        for right in range(n):
            while s[right] in char_str:
                char_str.remove(s[left])
                left += 1
            char_str.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

        
class Solution(object):
    def longestSubstring(self, s, k):
        n = len(s)
        freq = {}
        for ch in range(n):
            freq[s[ch]] = freq.get(s[ch],0) + 1
        for ch in freq:
            if freq[ch] < k:
                return max(self.longestSubstring(sub,k) for sub in s.split(ch))
        return len(s)



            
        
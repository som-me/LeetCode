class Solution(object):
    def findRepeatedDnaSequences(self, s):
        k = 10
        seen = set()
        result = set()
        for r in range(len(s) - k + 1):
            window = s[r:r+k]
            if window in seen:
                result.add(window)
            else:
                seen.add(window)    
        return list(result)

class Solution(object):
    def firstUniqChar(self, s):
        feq = {}
        for i,num in enumerate(s):
            if num not in feq:
                feq[num] = 1
            else:
                feq[num] -= 1

        for i,num in enumerate(s):
            if feq[num] == 1:
                return i
        return -1

        
        
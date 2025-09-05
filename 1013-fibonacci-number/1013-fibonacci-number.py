class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def helper(k):
            #base case
            if k == 0 or k == 1: return k

            #check if already present
            if dp[k] != -1: return dp[k]

            #recursive case
            dp[k] = helper(k-1) + helper(k-2)
            return dp[k]
        return helper(n)
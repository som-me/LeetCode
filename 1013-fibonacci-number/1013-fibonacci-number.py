class Solution:
    def fib(self, n: int) -> int:
        # We created a list for cache
        dp = [-1]*(n+1)
        # Lets use this list for storing the memoization values..
        def helper(i):
            #Base case:
            if i == 0:
                return 0
            if i == 1:
                return 1
            #Check if the value of i exists in the DP cache..
            if dp[i] != -1:
                return dp[i]
            #If dp[i] == -1 then, initailze it with the new value recursively and return dp[i]
            dp[i] = helper(i-1) + helper(i-2)
            return dp[i]
        return helper(n)
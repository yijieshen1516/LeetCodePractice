class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]

        return self.helper(n, dp)

    def helper(self, n, dp):

        if n == 0:
            return 1

        if n == 1:
            return 1

        if dp[n] > 0:
            return dp[n]

        count = 0
        for i in range(1, n+1):
            left = self.helper(i-1, dp)
            right = self.helper(n-i, dp)

            count += left * right

        dp[n] = count
        return dp[n]

n = 3
print(Solution().numTrees(n))
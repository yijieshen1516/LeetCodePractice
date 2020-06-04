
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        count = [0] * (amount + 1)

        res = self.helper(coins, count, amount)
        return res

    def helper(self, coins, count, rem):
        if rem < 0:
            return -1

        if rem == 0:
            return 0

        if count[rem] != 0:
            return count[rem]

        minval = float('inf')
        for i in range(len(coins)):
            k = self.helper(coins, count, rem - coins[i])
            if k >= 0 and k < minval:
                minval = k + 1

        if minval == float('inf'):
            count[rem] = -1
        else:
            count[rem] = minval

        return count[rem]

coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
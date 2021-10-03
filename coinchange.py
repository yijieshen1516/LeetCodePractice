
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
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

        """

#         coins.sort()
#         self.mem = {0:0}
#
#         minCoins = self.getMinCoins(coins, amount)
#
#         if minCoins == float('Inf'):
#             return -1
#
#         return minCoins
#
#
#     def getMinCoins(self, coins, amount):
#
#         if amount == 0:
#             return 0
#
#         if amount in self.mem:
#             return self.mem[amount]
#
#         minCoins = float('Inf')
#
#         for c in coins:
#             if amount - c < 0:
#                 break
#
#             numCoins = self.getMinCoins(coins, amount-c) +1
#             minCoins = min(numCoins, minCoins)
#
#         self.mem[amount] = minCoins
#
#         return minCoins
#
#
# coins = [1, 2, 5]
# amount = 11
# print(Solution().coinChange(coins, amount))

"""
recursion with mem

        self.seen = {}
        
        def getNumChange(amount):
            
            if amount == 0:
                return 0 
            
            if amount < 0: 
                return float('Inf')
            
            if amount in self.seen:
                return self.seen[amount]
            
            res = 1 + min(getNumChange(amount - c) for c in coins)
            self.seen[amount] = res
            return res
        
        r = getNumChange(amount)
        return r if r != float("inf") else -1
        """


def occurredOnce(arr, n):
    i = 1
    len = n

    # Check if the first and
    # last element is equal
    # If yes, remove those elements
    if arr[0] == arr[len - 1]:
        i = 2
        len -= 1

    # Start traversing the
    # remaining elements
    while i < n:

        # Check if current element is
        # equal to the element at
        # immediate previous index
        # If yes, check the same for
        # next element
        if arr[i] == arr[i - 1]:
            i += 1

        # Else print the current element
        else:
            print(arr[i - 1])

        i += 1

    # Check for the last element
    if (arr[n - 1] != arr[0] and
            arr[n - 1] != arr[n - 2]):
        print(arr[n - 1])

#arr = [7, 7, 8, 8, 9, 1, 1, 4, 2, 2]
arr = [-9, -8, 4, 4, 5, 5, -1]
n = len(arr)

print(occurredOnce(arr, n))
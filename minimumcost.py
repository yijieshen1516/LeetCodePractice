import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """

        heapq.heapify(sticks)
        sums = 0

        while len(sticks) > 1:

            num1 = heapq.heappop(sticks)
            num2 = heapq.heappop(sticks)

            sums += num1 + num2

            heapq.heappush(sticks, num1+num2)

        return sums

sticks = [2, 4, 3]
print(Solution().connectSticks(sticks))
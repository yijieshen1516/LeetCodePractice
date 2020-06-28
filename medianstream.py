import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return

        if num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        median = 0

        if len(self.small) > len(self.large):
            median = -self.small[0]
        elif len(self.small) == len(self.large):
            median = (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) < len(self.large):
            median = self.large[0]

        return median

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
num = 1
obj.addNum(num)
param_1 = obj.findMedian()
num = 2
obj.addNum(num)
param_2 = obj.findMedian()
num = 3
obj.addNum(num)
param_3 = obj.findMedian()
num = 4
obj.addNum(num)
param_4 = obj.findMedian()
num = 5
obj.addNum(num)

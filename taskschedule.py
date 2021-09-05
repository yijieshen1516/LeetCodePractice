from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            for _ in range(n):
                if h:
                    x,y = heappop(h)
                    curr_time += 1
                    if x != -1:
                        temp.append((x+1,y))
            for item in temp:
                heappush(h, item)
        return curr_time

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(Solution().leastInterval(tasks, n))

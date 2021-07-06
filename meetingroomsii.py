import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[0])

        heap = []

        heapq.heappush(heap, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, interval[1])

        return len(heap)


intervals = [[0, 30], [5, 10], [15, 20]]
print(Solution().minMeetingRooms(intervals))
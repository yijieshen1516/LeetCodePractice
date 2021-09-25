import heapq

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        maxWidth = min(len(grid), len(grid[0]))//2
        maxSizes = []

        for row in range(len(grid)):

            for col in range(len(grid[0])):

                for dist in range(maxWidth+1):

                    rhombus = self.getSize(grid, row, col, dist)

                    if rhombus > 0:

                        if rhombus not in maxSizes:
                            heapq.heappush(maxSizes, rhombus)

                        if len(maxSizes) > 3:
                            heapq.heappop(maxSizes)

        res = []

        while maxSizes:
            res.append(heapq.heappop(maxSizes))

        return res[::-1]


    def getSize(self, grid, row, col, dist):

        if dist == 0:
            return grid[row][col]

        summ = 0

        if col-dist < 0 or col+dist >= len(grid[0]) or row+(2*dist) >= len(grid):
            return 0

        for left in range(1, dist+1):
            summ += grid[row+left][col-left]

        row += dist
        col -= dist

        for bot in range(1, dist+1):
            summ += grid[row+bot][col+bot]

        row += dist
        col += dist

        for right in range(1, dist+1):
            summ += grid[row-right][col+right]

        row -= dist
        col += dist

        for top in range(1, dist+1):
            summ += grid[row-top][col-top]

        return summ

grid = [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]
print(Solution().getBiggestThree(grid))
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxarea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxarea = max(self.helper(grid, i, j), maxarea)

        return maxarea

    def helper(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = 0

        down = self.helper(grid, i + 1, j)
        up = self.helper(grid, i - 1, j)
        right = self.helper(grid, i, j + 1)
        left = self.helper(grid, i, j - 1)

        return down + up + right + left + 1


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

print(Solution().maxAreaOfIsland(grid))
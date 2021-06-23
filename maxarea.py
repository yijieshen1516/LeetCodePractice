class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    #     maxarea = 0
    #
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             maxarea = max(self.helper(grid, i, j), maxarea)
    #
    #     return maxarea
    #
    # def helper(self, grid, i, j):
    #
    #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
    #         return 0
    #
    #     grid[i][j] = 0
    #
    #     down = self.helper(grid, i + 1, j)
    #     up = self.helper(grid, i - 1, j)
    #     right = self.helper(grid, i, j + 1)
    #     left = self.helper(grid, i, j - 1)
    #
    #     return down + up + right + left + 1

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        max_area = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    queue = [(m, n)]
                    grid[m][n] = 0
                    area = 0
                    while queue:
                        row, col = queue.pop(0)
                        area += 1
                        for direction in directions:
                            new_row = row + direction[0]
                            new_col = col + direction[1]
                            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                                grid[new_row][new_col] = 0
                                queue.append((new_row, new_col))

                    max_area = max(max_area, area)

        return max_area


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

print(Solution().maxAreaOfIsland(grid))
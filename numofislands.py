class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    #     res = 0
    #
    #     for m in range(len(grid)):
    #         for n in range(len(grid[0])):
    #             if grid[m][n] == '1':
    #                 self.helper(grid, m, n)
    #                 res += 1
    #
    #     return res
    #
    # def helper(self, grid, i, j):
    #
    #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
    #         return
    #
    #     grid[i][j] = '0'
    #
    #     self.helper(grid, i + 1, j)
    #     self.helper(grid, i - 1, j)
    #     self.helper(grid, i, j + 1)
    #     self.helper(grid, i, j - 1)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    queue = [(m, n)]
                    while queue:
                        row, col = queue.pop(0)
                        for direction in directions:
                            new_row = row + direction[0]
                            new_col = col + direction[1]
                            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                                grid[new_row][new_col] = '0'
                                queue.append((new_row, new_col))
                    count += 1

        return count


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(Solution().numIslands(grid))
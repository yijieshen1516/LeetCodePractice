class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    self.helper(grid, m, n)
                    res += 1

        return res

    def helper(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'

        self.helper(grid, i + 1, j)
        self.helper(grid, i - 1, j)
        self.helper(grid, i, j + 1)
        self.helper(grid, i, j - 1)


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(Solution().numIslands(grid))
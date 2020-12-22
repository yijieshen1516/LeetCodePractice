class Solution():
    def numDistinctIslandas(self, grid):

        islands = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                    self.island = set()
                    self.helper(grid, i, j, start_i, start_j)

                if self.island not in islands:
                    islands.add(tuple(self.island))

        return len(islands)


    def helper(self, grid, i, j, start_i, start_j):

        if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0]) or grid[i][j] != 1:
            return

        self.island.add((i-start_i,j-start_j))
        grid[i][j] = 0

        self.helper(grid, i+1, j, start_i, start_j)
        self.helper(grid, i-1, j, start_i, start_j)
        self.helper(grid, i, j+1, start_i, start_j)
        self.helper(grid, i, j-1, start_i, start_j)

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

print(Solution().numDistinctIslandas(grid))
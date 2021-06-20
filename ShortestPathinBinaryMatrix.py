class Solution(object):

    def shortestPathBinaryMatrix(self, grid):

        queue = []
        queue.append((0, 0, 1))
        visited = {(0, 0)}

        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        while queue:

            row, col, distance = queue.pop(0)

            if (row, col) == (max_row, max_col):
                return distance

            for direction in directions:
                new_row = direction[0] + row
                new_col = direction[1] + col

                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue

                if grid[new_row][new_col] == 0:

                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, distance + 1))

        return -1



#grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[0,1,1,1,1,1,1,1], [0,1,1,0,0,0,0,0], [0,1,0,1,1,1,1,0], [0,1,0,1,1,1,1,0], [0,1,1,0,0,1,1,0], [0,1,1,1,1,0,1,0], [0,0,0,0,0,1,1,0], [1,1,1,1,1,1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))
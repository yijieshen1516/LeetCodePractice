import collections

class Solution(object):

    def largestIsland(self, grid):

        island_tag = 100
        area = collections.Counter()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        ret = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = [(i, j)]
                    island_tag += 1
                    grid[i][j] = island_tag

                    while queue:
                        row, col = queue.pop(0)
                        area[island_tag] += 1
                        for direction in directions:
                            new_row = row + direction[0]
                            new_col = col + direction[1]

                            if 0 <= new_row < len(grid) and 0<= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                                grid[new_row][new_col] = island_tag
                                queue.append((new_row, new_col))

        zero_pres = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    zero_pres = True
                    areanum = 1
                    islands = set()
                    for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy] != 0:
                            islands.add(grid[xx][yy])

                    for island in islands:
                        areanum += area[island]

                    ret = max(ret, areanum)

        return ret if zero_pres else len(grid) * len(grid[0])


# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 1]
# ]

grid = [[1, 1], [1, 0]]

print(Solution().largestIsland(grid))





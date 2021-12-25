class Solution(object):
    def shortestBridge(self, A):
        n, m = len(A), len(A[0])
        self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        stack = []
        found = False
        seen = set()

        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    self.dfs(n, m, i, j, stack, A, seen)
                    found = True
                    break

            if found:
                break

        ans = 0

        while stack:
            size = len(stack)
            level = []

            for s in range(size):
                i, j = stack.pop(0)

                for move in self.moves:
                    newI = i + move[0]
                    newJ = j + move[1]

                    if newI < 0 or newI >= n or newJ < 0 or newJ >= m or (newI, newJ) in seen:
                        continue

                    if A[newI][newJ] == 1:
                        return ans

                    seen.add((newI, newJ))
                    #level.append((newI, newJ))
                    stack.append((newI, newJ))

            ans += 1
            #stack = level
        return -1

    def dfs(self, n, m, i, j, stack, grid, seen):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1 or (i, j) in seen:
            return

        seen.add((i, j))
        stack.append((i, j))

        for move in self.moves:
            self.dfs(n, m, i + move[0], j + move[1], stack, grid, seen)



#grid = [[0, 1], [1, 0]]
grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(Solution().shortestBridge(grid))
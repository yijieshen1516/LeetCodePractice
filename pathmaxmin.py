
class Solution():

    def maximumMinimumPath(self, matrix):

        rl = len(matrix)
        cl = len(matrix[0])
        de = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def check(val):

            def dfs(x, y):

                if x == rl-1 and y == cl-1:
                    return True

                for i, j in de:
                    nx = x + i
                    ny = y + j
                    if 0<= nx < cl and 0<=ny < rl and dfs(nx, ny) and matrix[nx][ny] >=val:
                        return True

                return False

            return dfs(0, 0)

        ceiling = min(matrix[0][0], matrix[-1][-1])
        unique = set()
        for i in range(rl):
            for j in range(cl):
                if matrix[i][j] < ceiling:
                    unique.add(matrix[i][j])
        arr = sorted(unique)
        l, r = 0, len(arr)

        while l < r:
            m = (l+r) /2
            if check(arr[m]):
                l = m +1
            else:
                r = m - 1

        return arr[r]






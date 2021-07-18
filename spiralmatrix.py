class Solution(object):
    def spiralOrder(self, matrix):
        ans = []

        if len(matrix) == 0:
            return ans

        R = len(matrix)
        C = len(matrix[0])
        seen = [[0 for i in range(C)] for j in range(R)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = 0
        c = 0
        di = 0

        # Iterate from 0 to R * C - 1
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr = r + dr[di]
            cc = c + dc[di]

            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r = cr
                c = cc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
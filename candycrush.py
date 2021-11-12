class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        print(m, n)
        while True:
            # find the candies that can be crushed vertically
            v_crush = [[] for _ in range(n)]
            for j in range(n):
                i1 = 0
                while i1 < m:
                    i2 = i1 + 1
                    while i2 < m and board[i1][j] != 0 and board[i2][j] == board[i1][j]:
                        i2 += 1
                    if i2 - i1 >= 3:
                        v_crush[j].append([i1, i2])
                    i1 = i2
            # find the candies that can be crushed horizontally
            h_crush = [[] for _ in range(m)]
            for i in range(m):
                j1 = 0
                while j1 < n:
                    j2 = j1 + 1
                    while j2 < n and board[i][j1] != 0 and board[i][j2] == board[i][j1]:
                        j2 += 1
                    if j2 - j1 >= 3:
                        h_crush[i].append([j1, j2])
                    j1 = j2
            changes = 0
            # crush candies vertically
            for j in range(n):
                for i1, i2 in v_crush[j]:
                    changes += 1
                    for k in range(i1, i2):
                        board[k][j] = 0
            # crush candies horizontally
            for i in range(m):
                for j1, j2 in h_crush[i]:
                    changes += 1
                    for k in range(j1, j2):
                        board[i][k] = 0
            if changes == 0:
                return board
            # let candies drop down
            for j in range(n):
                candies = []
                for i in range(m):
                    if board[i][j] != 0:
                        candies.append(board[i][j])
                h = len(candies)
                for i in range(h):
                    board[m-1-i][j] = candies[h-1-i]
                for i in range(m - h):
                    board[i][j] = 0

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

print(Solution().candyCrush(board))
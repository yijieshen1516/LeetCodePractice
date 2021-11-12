from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        q = deque()

        for row in range(rows):
            q.append((row, 0))
            q.append((row, cols-1))

        for col in range(cols):
            q.append((0, col))
            q.append((rows-1, col))


        while q:
            r, c = q.popleft()
            if 0<=r<rows and 0<=c<cols and board[r][c] == 'O':
                board[r][c] = 'N'
                for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0<=i<rows and 0<=j<cols and board[i][j] == 'O':
                        board[i][j] = 'N'
                        q.append((i, j))

        print(board)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'N':
                    board[row][col] = 'O'


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(Solution().solve(board))
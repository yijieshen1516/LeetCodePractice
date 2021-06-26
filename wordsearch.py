class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for m in range(len(board)):
            for n in range(len(board[0])):
                if self.helper(board, word, m, n, 0):
                    return True

        return False

    def helper(self, board, word, i, j, d):

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[d] != board[i][j]:
            return False

        if d == len(word) - 1:
            return True

        cur = board[i][j]
        board[i][j] = 0
        ans = self.helper(board, word, i+1, j, d+1) or self.helper(board, word, i-1, j, d+1) or self.helper(board, word, i, j+1, d+1) or self.helper(board, word, i, j-1, d+1)

        board[i][j] = cur

        return ans


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
word = 'ABCCED'
print(Solution().exist(board, word))
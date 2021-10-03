class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == word[0]:
                    if self.dfs(board, m, n, 0, word, visited):
                        return True

        return False

    # def dfs(self,board,i,j,idx,word):
    #     if idx==len(word):
    #         return True
    #
    #     if i< 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j]!=word[idx]:
    #         return False
    #
    #     original=board[i][j]
    #     board[i][j]=""
    #
    #     if self.dfs(board,i-1,j,idx+1,word) or self.dfs(board,i+1,j,idx+1,word) or self.dfs(board,i,j-1,idx+1,word) or self.dfs(board,i,j+1,idx+1,word):
    #         return True
    #     else:
    #
    #         board[i][j]=original

    def dfs(self,board,i,j,idx,word, visited):

        if idx==len(word):
            return True

        if i< 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j]!=word[idx] or (i, j) in visited:
            return False

        visited.add((i,j))

        right = self.dfs(board, i+1, j, idx+1, word, visited)
        left = self.dfs(board, i-1, j, idx+1, word, visited)
        top = self.dfs(board, i, j+1, idx+1, word, visited)
        bott = self.dfs(board, i, j-1, idx+1, word, visited)

        visited.remove((i,j))

        return left or right or top or bott

#board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
#word = 'ABCCED'

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"

#board = [["a"]]
#word = "a"

print(Solution().exist(board, word))
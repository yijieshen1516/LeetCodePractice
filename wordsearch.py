class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == word[0]:
                    if self.dfs(board, m, n, 0, word):
                        return True

        return False

    def dfs(self,board,i,j,idx,word):
        if idx==len(word):
            return True

        if i< 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j]!=word[idx]:
            return False

        original=board[i][j]
        board[i][j]=""

        if self.dfs(board,i-1,j,idx+1,word) or self.dfs(board,i+1,j,idx+1,word) or self.dfs(board,i,j-1,idx+1,word) or self.dfs(board,i,j+1,idx+1,word):
            return True
        else:

            board[i][j]=original


#board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
#word = 'ABCCED'

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

#board = [["a"]]
#word = "a"

print(Solution().exist(board, word))
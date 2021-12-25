class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def maximalSquareMemo(matrix,i,j,cache):
            if i >= len(matrix) or j >= len(matrix[0]): return 0
            if matrix[i][j] == '0': cache[i][j] = 0
            if cache[i][j] != -1:
                return cache[i][j]
            else:
                cache[i][j] = min(maximalSquareMemo(matrix,i+1,j,cache),maximalSquareMemo(matrix,i+1,j+1,cache),maximalSquareMemo(matrix,i,j+1,cache)) + 1
            return cache[i][j]

        maxs = -float("inf")
        cache = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxs = max(maxs,maximalSquareMemo(matrix,i,j,cache))
        return maxs*maxs


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(matrix))
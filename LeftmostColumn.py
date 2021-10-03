class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = len(binaryMatrix), len(binaryMatrix[0])
        ans = cols

        for row in range(rows):

            l = 0
            r = cols - 1

            while l < r-1:
                mid = (l + r)/2

                if binaryMatrix[row][mid] == 0:
                    l = mid
                else:
                    r = mid

            if binaryMatrix[row][l] == 1:
                index = l
            elif binaryMatrix[row][r]== 1:
                index = r
            else:
                index = cols

            ans = min(ans, index)

        if ans == cols:
            return -1

        else:
            return ans


mat = [[0, 0], [1, 1]]
print(Solution().leftMostColumnWithOne(mat))

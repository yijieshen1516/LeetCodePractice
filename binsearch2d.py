class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ans = False

        for row in matrix:
            if row[0] > target or ans == True:
                return ans
            ans = self.binarysearch(row, target)

        return ans


    def binarysearch(self, row, target):

        left = 0
        right = len(row) -1

        while left < right:
            mid = (right + left) //2

            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid - 1
            else:
                return True

        return False

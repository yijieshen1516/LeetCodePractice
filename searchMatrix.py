class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ans = False

        for row in matrix:
            if not row or row[0] > target or ans == True:
                return ans
            ans = self.binarysearch(row, target)

        return ans

    def binarysearch(self, row, target):

        left = 0
        right = len(row) -1

        while left < right -1:
            mid = (right + left) //2

            if target >= row[mid]:
                left = mid
            elif target < row[mid]:
                right = mid

        if row[left] == target or row[right] == target:
            return True
        else:
            return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(Solution().searchMatrix(matrix, target))
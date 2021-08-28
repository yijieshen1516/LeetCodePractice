class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        prefixsum = {}
        prefixsum[0] = 1

        count = 0
        res = 0

        for num in A:

            res += num

            res = res % K

            if res in prefixsum:
                count += prefixsum[res]
                prefixsum[res] += 1
            else:
                prefixsum[res] = 1


        return res


A = [4, 5, 0, -2, -3, 1]
K = 5
print(Solution().subarraysDivByK(A, K))
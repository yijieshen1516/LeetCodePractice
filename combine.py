class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        curr = []

        self.bt(n, k, res, curr, 1)

        return res



    def bt(self, n, k, res, curr, pos):

        if k == len(curr):
            res.append(curr[:])
            return

        for i in range(pos, n-(k-len(curr))+2):
            curr.append(i)
            self.bt(n, k, res, curr, i+1)
            curr.pop()


n=4
k=4
print(Solution().combine(n, k))
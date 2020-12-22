class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        res = []
        self.high = 0
        self.bt(res, arr, 0)

        return self.high

    def bt(self, res, arr, k):
        self.high = max(self.high, len("".join(res)))

        for idx in range(k, len(arr)):
            res.append(arr[idx])
            tmp = "".join(res)
            if len(set(tmp)) == len(tmp):
                self.bt(res, arr, idx + 1)
            res.pop()


arr = ['un', 'iq', 'ue']
print(Solution().maxLength(arr))
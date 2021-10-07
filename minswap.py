class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        ones = sum(data)
        cnt_one = 0
        ans = 0
        i = 0
        j = 0

        while j < len(data):

            cnt_one += data[j]
            j += 1

            if j - i > ones:
                cnt_one -= data[i]
                i += 1

            ans = max(ans, cnt_one)

        return ones - ans


data = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
print(Solution().minSwaps(data))



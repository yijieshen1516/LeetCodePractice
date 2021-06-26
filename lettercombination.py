class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        """
        if not digits:
            return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        ans = []
        self.bt(ans, '', phone, 0, digits)

        return ans

    def bt(self, ans, string, phone, index, digits):

        if len(string) == len(digits):
            ans.append(string)
            return

        for idx in range(index, len(digits)):
            for word in phone[digits[idx]]:
                self.bt(ans, string + word, phone, idx+1, digits)

digits = '23'
print(Solution().letterCombinations(digits))
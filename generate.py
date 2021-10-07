class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        string = ''
        left = 0
        right = 0

        self.bt(ans, '', left, right, n)

        return ans


    def bt(self, ans, string, left, right, n):

        if len(string) == 2* n:
            ans.append(string)
            return

        if left < n:
            self.bt(ans, string+ '(', left + 1, right, n)

        if right < left:
            self.bt(ans, string + ')', left, right + 1, n)


n = 3
print(Solution().generateParenthesis(n))
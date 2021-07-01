class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []
        self.bt(s, [], res)
        return res


    def bt(self, s, curr, res):

        if len(s) == 0:
            res.append(curr[:]) #deep copy, always remember here


        for i in range(1, len(s) +1):
            if self.isPalindrome(s[:i]):
                curr.append(s[:i])
                self.bt(s[i:], curr, res)
                curr.pop()


    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1; r -= 1
        return True


s = "aab"
print(Solution().partition(s))
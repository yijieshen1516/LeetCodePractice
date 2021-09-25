class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        mem = {}

        return self.helper(s, t, 0, 0, mem)


    def helper(self, s, t, i, j, mem):

        if (i, j) in mem:
            return mem[i, j]

        if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
            return int(j == len(t))

        res = self.helper(s, t, i+1, j, mem)

        if s[i] == t[j]:
            res += self.helper(s, t, i+1, j+1, mem)

        mem[i, j] = res

        return res

s = 'rabbbit'
t = 'rabbit'

print(Solution().numDistinct(s, t))
class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """

        mem = {}
        return self.helper(s, 0, len(s), mem) <= k

    def helper(self, s, left, right, mem):
        if left == right or left+1 == right: # empty string or single letter
            return 0
        if (left, right) in mem:
            return mem[(left, right)]
        if s[left] == s[right-1]:
            mem[(left, right)] = self.helper(s, left+1, right-1, mem)
        else:
            mem[(left, right)] = min(self.helper(s, left+1, right, mem), self.helper(s, left, right-1, mem)) + 1
        return mem[(left, right)]


s = 'abcdeca'
k = 2
#s = 'baaaabaa'
#k = 3
print(Solution().isValidPalindrome(s, k))
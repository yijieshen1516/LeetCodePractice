class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        mem = {}

        return self.helper(s, wordDict, mem)

    def helper(self, s, wordDict, mem):

        if s in mem:
            return mem[s]

        if s in wordDict:
            mem[s] = True
            return True

        for idx in range(1, len(s)):

            left = s[:idx]
            right = s[idx:]

            if right in wordDict:
                mem[s] = self.helper(left, wordDict, mem)
                if mem[s]:
                    return True

        return False



#s = "leetcode"
#wordDict = ["leet", "code"]

s = "aaaaaaa"
wordDict = ["aaaa","aa"]

print(Solution().wordBreak(s, wordDict))
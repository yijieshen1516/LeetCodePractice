from collections import defaultdict


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mem = defaultdict(list)

        return self.helper(s, wordDict, mem)


    def helper(self, s, wordDict, mem):

        if not s:
            return []

        if s in mem:
            return mem[s]

        if s in wordDict:
            mem[s].append(s)
            return mem[s]

        for idx in range(1, len(s)):
            left = s[:idx]
            right = s[idx:]

            if right in wordDict:
                res = self.helper(left, wordDict, mem)
                for ss in res:
                    mem[s].append(right + 'and' + ss)


        return mem[s]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

print(Solution().wordBreak(s, wordDict))
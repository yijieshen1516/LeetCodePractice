from collections import defaultdict


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {}
        return self.memo_dfs(s, wordDict, memo)

    def memo_dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) ==0:
            return []

        s_partitions = []
        if s in wordDict:
            s_partitions.append(s)

        for cut_index in range(1, len(s)):
            partition = s[:cut_index]
            if partition not in wordDict:
                continue

            for following_partition in self.memo_dfs(s[cut_index:], wordDict, memo):
                s_partitions.append(partition + ' ' + following_partition)

        memo[s] = s_partitions
        print(s, memo[s])
        return s_partitions

#s = "catsanddog"
#wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))



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

            if left in wordDict:
                res = self.helper(right, wordDict, mem)
                for ss in res:
                    mem[s].append(left + ' ' + ss)

        return mem[s]"""


"""
backtracking time consuming is more than dfs + memo
"""
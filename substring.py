from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter_t = Counter(t)
        counter = 0

        i, j = 0, 0
        ans = float("inf"), None, None

        while j < len(s):

            if s[j] in counter_t:
                counter_t[s[j]] -= 1
                if counter_t[s[j]] == 0:
                    counter += 1

            while i <= j and counter == len(counter_t):

                if j - i + 1 < ans[0]:
                    ans = (j - i + 1, i, j)

                if s[i] in counter_t:
                    counter_t[s[i]] += 1

                    if counter_t[s[i]] > 0:
                        counter -= 1

                i += 1

            j += 1

        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]: ans[2] + 1]


S = "ab"
T = "a"
print(Solution().minWindow(S, T))
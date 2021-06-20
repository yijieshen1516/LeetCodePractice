from collections import Counter


# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         counter_t = Counter(t)
#         counter = 0
#
#         i, j = 0, 0
#         ans = float("inf"), None, None
#
#         while j < len(s):
#
#             if s[j] in counter_t:
#                 counter_t[s[j]] -= 1
#                 if counter_t[s[j]] == 0:
#                     counter += 1
#
#             while i <= j and counter == len(counter_t):
#
#                 if j - i + 1 < ans[0]:
#                     ans = (j - i + 1, i, j)
#
#                 if s[i] in counter_t:
#                     counter_t[s[i]] += 1
#
#                     if counter_t[s[i]] > 0:
#                         counter -= 1
#
#                 i += 1
#
#             j += 1
#
#         if ans[0] == float('inf'):
#             return ""
#         else:
#             return s[ans[1]: ans[2] + 1]

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicts = {}

        for alpha in t:

            if alpha in dicts:
                dicts[alpha] += 1
            else:
                dicts[alpha] = 1

        i, j = 0, 0
        ans = float('Inf'), None, None

        counter = 0

        while j < len(s):

            if s[j] in dicts:

                dicts[s[j]] -= 1
                if dicts[s[j]] == 0:
                    counter += 1

            while i <= j and counter == len(dicts):

                ans = min(ans[0], j-i+1), i, j

                if s[i] in  dicts:
                    dicts[s[i]] += 1

                    if dicts[s[i]] >= 1:
                        counter -= 1

                i += 1

            j += 1

        return s[ans[1] : ans[2]+1]


#S = "ADOBECODEBANC"
#T = "ABC"
S = ""

print(Solution().minWindow(S, T))
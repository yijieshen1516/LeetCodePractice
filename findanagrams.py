from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        i, j = 0, 0
        counter_p = Counter(p)
        counter = 0
        ans = []

        while j < len(s):

            if s[j] in counter_p:

                counter_p[s[j]] -= 1

                if counter_p[s[j]] == 0:
                    counter += 1

            while i <= j and counter == len(counter_p):

                if j - i + 1 == len(p):
                    ans.append(i)

                if s[i] in counter_p:
                    counter_p[s[i]] += 1

                    if counter_p[s[i]] > 0:
                        counter -= 1

                i += 1

            j += 1

        return ans


s = 'cbaebabacd'
p = 'abc'

print(Solution().findAnagrams(s,p))
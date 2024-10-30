import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        unique_count = len(set(s))
        maxLen = 0

        for count in range(1, unique_count+1):
            l, r, num_formed = 0, 0, 0
            count_map = collections.defaultdict(int)

            while r<len(s):
                count_map[s[r]] += 1
                if count_map[s[r]]==k:
                    num_formed += 1
                if num_formed==count and len(count_map)==count:
                    maxLen = max(maxLen, r-l+1)

                # minimize window for unique chars limit
                while l<r and len(count_map)>count:
                    if count_map[s[l]]==k:
                        num_formed -= 1
                    if count_map[s[l]]==1:
                        del count_map[s[l]]
                    else:
                        count_map[s[l]] -= 1
                    l += 1

                r += 1

            return maxLen

s = 'aaabb'
k = 3
print(Solution().longestSubstring(s, k))

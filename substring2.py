class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        i, j = 0, 0

        map_dict = {}
        max_length = 0

        while j < len(s):

            if s[j] in map_dict:
                map_dict[s[j]] += 1
            else:
                map_dict[s[j]] = 1

            while len(map_dict) > k:

                if s[i] in map_dict:
                    map_dict[s[i]] -= 1
                    if map_dict[s[i]] == 0:
                        del map_dict[s[i]]
                else:
                    map_dict[s[i]] = 1

                i += 1

            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length


s = 'eceba'
k = 2

print(Solution().lengthOfLongestSubstringKDistinct(s,k))
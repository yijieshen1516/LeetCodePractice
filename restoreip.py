class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ans = []
        curr = []

        self.bt(s, 0, 4, curr, ans)

        return ans

    def bt(self, s, idx, remain, curr, ans):

        if remain == 0:
            if idx == len(s):
                ans.append(".".join(curr))

            return

        for i in range(1, 4):
            if idx + i > len(s):
                break

            subs = s[idx: idx+i]

            if int(subs) <= 255:
                if i > 1 and subs[0] == '0':
                    continue

                curr.append(subs)
                self.bt(s, idx+i, remain-1, curr, ans)
                curr.pop()


s = '25525511135'
print(Solution().restoreIpAddresses(s))

# ans = []
# self.bt(ans, '', 0, 4, s)
#
# return ans
#
#
# def bt(self, ans, res, index, remain, s):
#     print(index)
#
#     if remain == 0:
#         if index == len(s):
#             ans.append(res)
#
#         return
#
#     for i in range(1, 4):
#         if index + i > len(s):
#             break
#
#         subs = s[index:index + i]
#
#         if int(subs) <= 255:
#             if res != '':
#                 self.bt(ans, res + '.' + str(subs), index + i, remain - 1, s)
#             else:
#                 self.bt(ans, res + str(subs), index + i, remain - 1, s)

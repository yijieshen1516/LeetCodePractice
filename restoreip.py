class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.bt(ans, '', 0, 4, s)

        return ans

    def bt(self, ans, res, index, remain, s):

        print(index)

        if remain == 0:
            if index == len(s):
                ans.append(res)

            return

        for i in range(1, 4):
            if index + i > len(s):
                break

            subs = s[index:index + i]

            if int(subs) <= 255:
                if  res != '':
                    self.bt(ans, res + '.' + str(subs), index + i, remain - 1, s)
                else:
                    self.bt(ans, res + str(subs), index + i, remain -1, s)

s = '25525511135'
print(Solution().restoreIpAddresses(s))

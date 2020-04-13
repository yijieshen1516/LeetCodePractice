class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]

        """

        l = 0
        r = 0

        for i in s:
            if i == '(':
                l += 1
            if i == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1

        answers = []
        self.bt(answers, l, r, s)

        return answers

    def isvalid(self, s):

        count = 0

        for i in s:
            if i == '(': count += 1
            if i == ')': count -= 1
            if count < 0: return False
        return True

    def bt(self, answers, l, r, nums):
        if l == 0 and r == 0 and self.isvalid(nums):
            answers.append(nums)
            return

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] == '(' and l > 0:
                self.bt(answers, l - 1, r, nums[:i] + nums[i + 1:])
            if nums[i] == ')' and r > 0:
                self.bt(answers, l, r - 1, nums[:i] + nums[i + 1:])



s = ")("

print(Solution().removeInvalidParentheses(s))

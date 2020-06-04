class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for ch in s:
            if ch == "(" or ch == "*":
                stack.append(ch)
            else:
                if len(stack)>0:
                    stack.pop()
                else:
                    return False

        stack2 = []

        for ch in s[::-1]:
            if ch == "*" or ")":
                stack2.append(ch)
            else:
                if stack2:
                    stack2.pop()
                else:
                    return False

        return True

s = ")("
print(Solution().checkValidString(s))
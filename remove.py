class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        indexes = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes.add(i)
            else:
                stack.pop()

        indexes = indexes.union(set(stack))

        string_s = []
        for i, c in enumerate(s):
            if i not in indexes:
                string_s.append(c)
        return ''.join(string_s)


#s = "lee(t(c)o)de)"
s = "))(("
Solution().minRemoveToMakeValid(s)
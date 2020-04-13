class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        for part in path.split('/'):

            if part == '..':
                if stack:
                    stack.pop()
            elif part == '.' and stack:
                continue
            elif part == '':
                continue
            else:
                stack.append(part)

        if len(stack) == 0:
            final_str = "/"

        if len(stack) == 1:
            final_str = "/" + stack[0]

        if len(stack) > 1:
            final_str = "/" + "/".join(stack)

        return final_str

path = '/a/./b/../../c/'
Solution().simplifyPath(path)
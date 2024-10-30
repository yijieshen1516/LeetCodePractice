class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]

        def isValid(expr):
            count = 0
            for ch in expr:
                if ch not in '()':
                    continue
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        q = [s]
        visited = set()
        visited.add(s)
        output = []
        found = False

        while q:

            expr = q.pop(0)

            if isValid(expr):
                output.append(expr)
                found = True

            if found:
                continue

            for i in range(len(expr)):
                if expr[i] not in '()':
                    continue

                candidate = expr[:i] + expr[i+1:]
                if candidate not in visited:
                    q.append(candidate)
                    visited.add(candidate)

        return output if output else ['']
        """
        left_rem = 0
        right_rem = 0

        # count bad left and right brackets
        for i, c in enumerate(s):
            if c == "(":
                left_rem += 1
            elif c == ")":
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        def helper(index, left_so_far, right_so_far, left_rem, right_rem, s_so_far):

            # stopping condition
            if index == len(s):
                # check for validity that no bad left or right brackets are remaining
                if left_rem == 0 and right_rem == 0:
                    results.add(s_so_far)
                return

            # either remove one bad left bracket or do nothing and proceed
            if s[index] == "(" and left_rem > 0:
                helper(index+1, left_so_far, right_so_far, left_rem-1, right_rem, s_so_far)
            # either remove one bad right bracket or do nothing and proceed
            if s[index] == ")" and right_rem > 0:
                helper(index+1, left_so_far, right_so_far, left_rem, right_rem-1, s_so_far)

            if s[index] == "(":
                helper(index+1, left_so_far+1, right_so_far, left_rem, right_rem, s_so_far + "(")
            elif s[index] == ")":
                if left_so_far > right_so_far:
                    helper(index+1, left_so_far, right_so_far+1, left_rem, right_rem, s_so_far + ")")
            else: # any other char, use as-is
                helper(index+1, left_so_far, right_so_far, left_rem, right_rem, s_so_far + s[index])

            return


        results = set()
        helper(0, 0, 0, left_rem, right_rem, "")

        return list(results)



s = '()())()'
print(Solution().removeInvalidParentheses(s))

class Solution(object):
    def addOperators(self, num, target):

        def dfs(idx, expr, curr, prev, ans):

            if idx == len(num):
                if curr == target:
                    ans.append(expr)
                return

            for i in range(idx+1, len(num)+1):
                s = num[idx:i]
                x = int(num[idx:i])
                if prev == None:
                    dfs(i, s, x, x, ans)
                else:
                    dfs(i, expr+'+'+s, curr+x, x, ans)
                    dfs(i, expr+'-'+s,curr-x, x, ans)
                    dfs(i, expr+'*'+s, curr)







num = '123'
target = 6

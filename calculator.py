class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        s += '+'

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    tmp = stack.pop()*num
                    stack.append(tmp)
                elif sign == '/':
                    tmp1 = stack.pop()
                    tmp = float(tmp1)/num
                    stack.append(int(tmp))

                num = 0
                sign = ch

        return sum(stack)
#s = '3-2*3'
#s = '42'
s = '14-3/2'
print(Solution().calculate(s))


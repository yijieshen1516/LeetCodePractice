class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)
        if not self.maxstack or x >= self.maxstack[-1]:
            self.maxstack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        x = self.stack.pop()
        if self.maxstack and  x == self.maxstack[-1]:
            self.maxstack.pop()

        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        if self.maxstack:
            return self.maxstack[-1]


    def popMax(self):
        """
        :rtype: int
        """

        temp = []
        while self.stack[-1] != self.maxstack[-1]:
            temp.append(self.stack[-1])
            self.stack.pop()
        out = self.stack.pop()
        self.maxstack.pop()
        while temp:
            self.push(temp[-1])
            temp.pop()
        return out


stk = MaxStack()
print(stk.push(5))
print(stk.push(1))
print(stk.popMax())
print(stk.peekMax())
class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

class Solution(object):
    def level(self, root):
        q = [root]
        next = []
        line = []
        while q:
            head = q.pop(0)
            if head.left:
                next.append(head.left)
            if head.right:
                next.append(head.right)
            line.append(head.val)
            if not q:
                print(line)
                if next:
                    q = next
                    next = []
                    line = []

    def preorder(self, root):
        output = []
        if not root:
            return output

        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if count == 1:
                output.append(node.val)
                stack.append((node, count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:
                if node.right:
                    stack.append((node.right, 1))

        return output


root = None
root = newNode(4)
root.left = newNode(2)
root.right = newNode(9)
root.left.left = newNode(3)
root.left.right = newNode(8)
root.right.right = newNode(7)

Solution().preorder(root)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def constructFromPrePost(self, pre, post):

        return self.helper(pre, post)


    def helper(self, pre, post):

        if not pre:
            return None

        curr = post.pop()
        node = TreeNode(curr)

        if len(pre) == 1:
            return node

        idx = pre.index(post[-1])

        node.right = self.helper(pre[idx:], post)
        node.left = self.helper(pre[1:idx], post)

        return node

pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]

print(Solution().constructFromPrePost(pre, post).val)
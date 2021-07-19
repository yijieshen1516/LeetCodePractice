# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1

        def dfs(root, cur_sum):
            if not root:
                return
            cur_sum += root.val
            self.ans += cache[cur_sum - sum]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            cache[cur_sum] -= 1

        dfs(root, 0)
        return self.ans

sum = 8
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)

print(Solution().pathSum(root, sum))


# if not root:
#     return 0
#
# return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
#
# def helper(self, root, sum):
#
#     count = 0
#
#     if not root:
#         return 0
#
#     sum -= root.val
#
#     if sum == 0:
#         count += 1
#
#     count += self.helper(root.left, sum)
#     count += self.helper(root.right, sum)
#
#     return count
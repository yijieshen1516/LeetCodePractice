import collections
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isCompleteTree(self, root):
        traversal_queue = collections.deque( [ root ] )
        prev_node = root

        # Launch Level-order traversal

        while traversal_queue:

            cur_node = traversal_queue.popleft()

            if cur_node:

                if not prev_node:
                    # Empty node in the middle means this is not a complete binary tree ( not left-compact)
                    return False

                traversal_queue.append( cur_node.left )
                traversal_queue.append( cur_node.right )

            # update previous node
            prev_node = cur_node

        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right= TreeNode(7)
print(Solution().isCompleteTree(root))
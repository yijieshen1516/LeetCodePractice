# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def str2tree(self, s):
        def recur(s):
            #check empty string
            if not s: return
            #s[..left]: value
            #s[left..right]: left subtree
            #s[right..]: right subtree
            left = right = len(s)
            bal = 0
            for i in range(len(s)):
                if s[i] == '(':
                    bal += 1
                if s[i] == ')':
                    bal -= 1
                if s[i] == '(' and bal == 1:
                    if left == len(s):
                        left = i
                    else:
                        right = i
            #return current node
            this = TreeNode(int(s[:left]))
            this.left = recur(s[left+1:right-1])
            this.right = recur(s[right+1:-1])
            return this

        return recur(s)

s = '4(2(3)(1))(6(5))'
print(Solution().str2tree(s))

"""
        if not s or len(s) == 0:
            return None
        root, _ = self.helper(s, 0)
        return root
    
    
    
    def helper(self, s, i):
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()): # negative sign or digit
            i += 1
        node = TreeNode(int(s[start : i]))
        if i < len(s) and s[i] == '(':
            i += 1 # skip '('
            node.left, i = self.helper(s, i)
            i += 1 # skip ')'
        if i < len(s) and s[i] == '(': # still has '(', create right tree
            i += 1 # skip '('
            node.right, i = self.helper(s, i)
            i += 1 # skip ')'
        return node, i
            
"""
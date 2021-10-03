mydict = {
    "carl": [40, 2],
    "alan": [2, 3],
    "bob": [2, 1],
    "danny": [3, 4],
}

#print(mydict.items())
#print(sorted(mydict.items(), key=lambda x:x[0]))
#print(sorted(mydict.items(), key=lambda x:x[1][0], reverse=True))
#print(sorted(mydict.items(), key=lambda x: [-x[1][0], x[0]], reverse=False))
#print(ord('a'))

#from collections import deque

#queue = deque([1, 2])

#print(queue.popleft())

# from collections import defaultdict
#
# mydict = defaultdict(int)
#
# mydict[1] = 1
# mydict[2] = 7
# mydict[3] = -1
#
# print(mydict.items())
# print(max(mydict.items(), key=lambda k:k[1]))


# def isBalanced(s):
#     # Write your code here
#
#     bracketMap = {'{': '}', '[': ']', '(': ')'}
#
#     stack = []
#
#     for ch in s:
#         if ch in ['{', '[', '(']:
#             stack.append(ch)
#         else:
#             if stack and ch == bracketMap[stack[-1]]:
#                 stack.pop()
#             else:
#                 return False
#
#     if len(stack) == 0:
#         return True
#
#     else:
#         return False
#
# s = '{{[[(())]]}}'
# print(isBalanced(s))
#
# class newNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# def insertLevelOrder(arr, i, n):
#
#     if i >= n:
#         return
#
#     node = newNode(arr[i])
#
#     node.left = insertLevelOrder(arr, 2*i+1, n)
#     node.right = insertLevelOrder(arr, 2*i+2, n)
#
#     return node
#
# def inOrder(root):
#
#     if not root:
#         return
#
#     inOrder(root.left)
#     print(root.val)
#     inOrder(root.right)
#
# arr = [1, 2, 3, 4, 5, 6, 8, 9]
# node = insertLevelOrder(arr, 0, len(arr))
# inOrder(node)
# import collections
#
# def numberofPairs(arr, k):
#
#     counter_a = collections.Counter(arr)
#     ans = 0
#
#     for num in arr:
#
#         if k - num != k/2:
#
#             if k - num in counter_a:
#                 ans += counter_a[k-num]
#         else:
#             ans += counter_a[k-num] * (counter_a[k-num] -1)
#
#     return ans//2
#
# arr = [1, 2, 3, 4, 3]
# k = 6
# print(numberofPairs(arr, k))


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

#
# def canGetExactChange(targetMoney, denominations):
#     # Write your code here
#     return helper(targetMoney, denominations, 0, 0)
#
#
# def helper(targetMoney, demoinations, curr, pos):
#
#     if curr > targetMoney:
#         return
#
#     if curr == targetMoney:
#         return True
#
#     else:
#
#         for idx in range(pos, len(demoinations)):
#             helper(targetMoney, demoinations, curr+demoinations[idx], idx)
#
#     return False
#
# targetMoney = 75
# denominations = [4, 17, 29]
# print(canGetExactChange(targetMoney, denominations))

# class TreeNode():
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def findEncryptedWord(s):
#     # Write your code here
#
#     s = list(s)
#     res = []
#
#     res = helper(s, res)
#
#     return ''.join(res)
#
#
# def helper(s, res):
#
#     if len(s) == 0:
#         return None
#
#     l = 0
#     r = len(s) -1
#
#     m = (l+r)//2
#
#     curr = s[m]
#     node = TreeNode(curr)
#
#     res.append(node.val)
#
#     node.left = helper(s[:m], res)
#     node.right = helper(s[m+1:], res)
#
#     return res
#
# s = 'abcd'
# print(findEncryptedWord(s))

# def getMilestoneDays(revenues, milestones):
#     # Write your code here
#     revAchievedDay = []
#     milestoneIdx = 0
#     prefixSum = 0
#     milestoneMap = dict()
#     for i, mileS in enumerate(milestones):
#         milestoneMap[mileS] = i
#
#     milestones.sort() # O(mlogm)
#
#     for i, rev in enumerate(revenues): # O(m + n)
#         prefixSum += rev
#         while milestoneIdx < len(milestones) and prefixSum >= milestones[milestoneIdx]:
#             revAchievedDay.append(i+1)
#             milestoneIdx += 1
#
#         if milestoneIdx == len(milestones):
#             break
#
#     ans = [0 for _ in range(len(milestones))]
#
#     for i, day in enumerate(revAchievedDay): # O(m)
#         ans[milestoneMap[milestones[i]]] = day
#
#     return ans
import bisect

def waysToSplit(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prefix = [0] * len(nums)
    prefixSum = 0

    for idx, num in enumerate(nums):
        prefixSum += num
        prefix[idx] = prefixSum

    ans = 0

    for i in range(0, len(nums)):
        j = bisect.bisect_left(prefix, 2*prefix[i])
        k = bisect.bisect_right(prefix, (prefix[i] + prefix[-1])//2)
        ans += max(0, min(len(nums), k) - max(i+1, j))
        print(ans)
    return ans % (10**9+7)

#nums = [1, 1, 1]
#print(waysToSplit(nums))
nums = [1, 2, 2, 2, 5, 0]
print(waysToSplit(nums))
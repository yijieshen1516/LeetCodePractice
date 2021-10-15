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
# import bisect
#
# def waysToSplit(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     prefix = [0] * len(nums)
#     prefixSum = 0
#
#     for idx, num in enumerate(nums):
#         prefixSum += num
#         prefix[idx] = prefixSum
#
#     ans = 0
#
#     for i in range(0, len(nums)):
#         j = bisect.bisect_left(prefix, 2*prefix[i])
#         k = bisect.bisect_right(prefix, (prefix[i] + prefix[-1])//2)
#         ans += max(0, min(len(nums), k) - max(i+1, j))
#         print(ans)
#     return ans % (10**9+7)
#
# #nums = [1, 1, 1]
# #print(waysToSplit(nums))
# nums = [1, 2, 2, 2, 5, 0]
# print(waysToSplit(nums))
#
# def badNumberes(arr, lower, upper):
#
#     maxlength = 0
#     arr.sort()
#     for idx in range(len(arr)):
#         length = 0
#         if idx == 0 and arr[idx] >= lower:
#             length = arr[idx] - lower
#         elif idx >= 1 and arr[idx] >= lower:
#             length = arr[idx] - max(lower, arr[idx-1]+1)
#         elif arr[idx] < upper:
#             length = max(0, min(arr[idx], upper) - arr[idx-1])
#
#         maxlength = max(maxlength, length)
#
#     return maxlength
#
#
# arr = [37, 7, 22, 15, 49, 60]
# lower = 3
# upper = 48
# print(badNumberes(arr, lower, upper))

# arr = [1, 2, 1, 3, 4, 3, 2]
# result = arr[0]
# for idx in range(1, len(arr)):
#     result ^= arr[idx]
# print(result)

# str = "abbbaaca"
#
# def remove(str):
#     if not str or len(str) < 1:
#         return
#
#     stack = []
#     fast = 0
#
#     while fast < len(str):
#         c = str[fast]
#         if len(stack) > 0 and str[fast] == stack[-1]:
#             while fast < len(str) and c == str[fast]:
#                 fast += 1
#             stack.pop()
#         else:
#             stack.append(str[fast])
#             fast += 1
#     return "".join(stack)
#
# print(remove(str))

# def findKthPositive(arr, k):
#     """
#     :type arr: List[int]
#     :type k: int
#     :rtype: int
#     """
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left+right)//2
#         missing = arr[mid] - mid -1
#
#         if missing < k:
#             left = mid + 1
#
#         else:
#             right = mid - 1
#
#     return right + k +1
#
# arr = [2, 3, 4, 7, 11]
# k = 5
#
# print(findKthPositive(arr, k))
# import random
#
# def findKthLargest(nums, k):
#     """
#     kth largest element using k size min heap
#     """
#
#     def partition(left, right, pivot_index):
#
#         pivot = nums[pivot_index]
#         nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
#
#         store_index = left
#         for i in range(left, right):
#             if nums[i] < pivot:
#                 nums[store_index], nums[i] = nums[i], nums[store_index]
#                 store_index += 1
#         nums[right], nums[store_index] = nums[store_index], nums[right]
#
#         return store_index
#
#     def select(left, right, k_smallest):
#
#         if left == right:
#             return nums[left]
#
#         pivot_index = random.randint(left, right)
#
#         pivot_index = partition(left, right, pivot_index)
#
#         if k_smallest == pivot_index:
#             return nums[k_smallest]
#         elif k_smallest < pivot_index:
#             return select(left, pivot_index-1, k_smallest)
#         else:
#             return select(pivot_index+1, right, k_smallest)
#
#     return select(0, len(nums)-1, len(nums)-k)
#
#
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(findKthLargest(nums, k))





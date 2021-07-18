
class Solution(object):
    def numIslands2(self, m, n, positions):
        disJointSet = DisJointSet()
        disJointSet.forest = [1] * (m*n)
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in positions:
            index = x * n + y
            disJointSet.setParent(index)
            for i, j in directions:
                a, b = x + i, y + j
                if 0 <= a < m and 0 <= b < n and a * n + b in disJointSet.parents:
                    disJointSet.Union(index, a * n + b)
            res.append(disJointSet.count)
        return res

class DisJointSet(object):

    def __init__(self):
        self.parents = {}
        self.count = 0
        self.forest = []

    def Union(self, x, y):
        set1 = self.find(x)
        set2 = self.find(y)
        if set1 != set2:
            if self.forest[set1] < self.forest[set2]:
                self.parents[set1] = set2
                self.forest[set2] += self.forest[set1]
            else:
                self.parents[set2] = set1
                self.forest[set1] += self.forest[set2]
            self.count -= 1

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

    def setParent(self, x):
        if self.parents.get(x):
            return
        self.parents[x] = x
        self.count += 1


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(Solution().numIslands2(m, n, positions))
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def minimumCost(self, N, connections):
        neighbor = defaultdict(list)
        for i, j, c in connections:
            neighbor[i].append((j, c))
            neighbor[j].append((i, c))
        #print(nbrs)
        res = 0
        mini_heap = [(0,1)]
        visited = set()
        while mini_heap:
            c, i = heappop(mini_heap)
            if i in visited:
                continue
            else:
                visited.add(i)
                res += c
                if len(visited) == N:
                    return res
                else:
                    for j, c in neighbor[i]:
                        if j in visited:
                            continue
                        else:
                            heappush(mini_heap, (c, j))
        return -1

N = 3
connections = [[1,2,5], [1,3,6], [2,3,1]]

print(Solution().minimumCost(N, connections))
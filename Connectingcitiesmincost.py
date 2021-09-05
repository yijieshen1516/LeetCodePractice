from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    # def minimumCost(self, N, connections):
    #     neighbor = defaultdict(list)
    #     for i, j, c in connections:
    #         neighbor[i].append((j, c))
    #         neighbor[j].append((i, c))
    #     #print(nbrs)
    #     res = 0
    #     mini_heap = [(0,1)]
    #     visited = set()
    #     while mini_heap:
    #         c, i = heappop(mini_heap)
    #         if i in visited:
    #             continue
    #         else:
    #             visited.add(i)
    #             res += c
    #             if len(visited) == N:
    #                 return res
    #             else:
    #                 for j, c in neighbor[i]:
    #                     if j in visited:
    #                         continue
    #                     else:
    #                         heappush(mini_heap, (c, j))
    #     return -1

    def minimumCost(self, N, connections):
        '''
        Kruskal's Algorithm:
        1) Create a forest F (a set of trees), where each vertex in
        the graph is a separate tree.
        2) Create a set S containing all the edges in the graph.
        3) While S is nonempty and F is not yet spanning (fully connected):
            3A) Remove an edge with minimum weight from S
            3B) If the removed edge connects two different trees then
            add it to the forest F, combining two trees into a single tree.
        '''
        def find(city):
            # Recursively re-set city's parent to its parent's parent.
            # Build the bush: ideally each tree/set is of height 1.
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parent[root2] = root1  # Always join roots!
            return True

        # [1] Keep track of disjoint sets. Initially each city is its own set.
        parent = {city: city for city in range(1, N+1)}
        # [2] Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:  # [3A]
            if union(city1, city2):  # [3B]
                total += cost
        # Check that all cities are connected.
        root = find(N)
        return total if all(root == find(city) for city in range(1, N+1)) else -1

N = 3
connections = [[1,2,5], [1,3,6], [2,3,1]]

print(Solution().minimumCost(N, connections))


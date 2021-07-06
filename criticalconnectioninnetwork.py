from collections import defaultdict

"""
class Solution:

    rank = {}
    graph = defaultdict(list)
    conn_dict = {}

    def criticalConnections(self, n, connections):

        self.formGraph(n, connections)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node, discovery_rank):

        # That means this node is already visited. We simply return the rank.
        if self.rank[node]:
            return self.rank[node]

        # Update the rank of this node.
        self.rank[node] = discovery_rank

        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:

            # Skip the parent.
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            # Recurse on the neighbor.
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def formGraph(self, n, connections):

        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}

        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None

        for edge in connections:

            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

            self.conn_dict[(min(u, v), max(u, v))] = 1
"""

class Solution():

    def criticalConnections(self, n, connections):

        self.graph = defaultdict(list)

        for edge in connections:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        self.res = []
        self.visited = set()
        self.low = {}
        self.dfs(0, -1, 0)

        return self.res

    def dfs(self, id, prevNode, node):
        self.visited.add(node)
        self.low[node] = id

        for nei in self.graph[node]:
            if nei == prevNode:
                continue

            if nei not in self.visited:
                self.dfs(id+1, node, nei)

            self.low[node] = min(self.low[node], self.low[nei])
            if id < self.low[nei]:
                self.res.append([node, nei])


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

print(Solution().criticalConnections(n, connections))
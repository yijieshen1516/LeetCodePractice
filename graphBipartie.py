class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        queue = [0]
        color = [0] * len(graph)
        color[0] = 1

        for i in range(1, len(graph)):

            while queue:

                curr = queue.pop(0)
                for node in graph[curr]:

                    if color[node] == color[curr]:
                        return False

                    if color[node] == 0:
                        color[node] = -color[curr]
                        queue.append(node)
        return True

#graph = [[1,3], [0, 2], [1, 3], [0, 2]]
graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(Solution().isBipartite(graph))
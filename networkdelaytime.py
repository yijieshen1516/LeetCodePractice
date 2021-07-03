import collections

class Solution:
    def networkDelayTime(self, times, N, K):
        adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
        for n1, n2, time in times:
            adj_matrix[n1-1][n2-1] = time

        queue = [(0, K-1)]
        t = [float('inf')] * N

        while queue:

            time, node = queue.pop(0)

            if time < t[node]:
                t[node] = time

                for nei in range(N):
                    if adj_matrix[node][nei] > 0:
                        queue.append((adj_matrix[node][nei] + time, nei))

        mx = max(t)

        return mx if mx < float('inf') else -1


times = [[2,1,1], [2,3,1], [3,4,1]]
N=4
K=2

print(Solution().networkDelayTime(times, N, K))
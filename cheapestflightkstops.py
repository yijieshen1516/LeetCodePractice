import heapq
import collections

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, K):

        adj_list = collections.defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v,w))

        best_visited = collections.defaultdict(lambda : 'Inf')

        prior_queue = [ (0, -1, src) ] #weight, steps, node

        while prior_queue:
            cost, steps, node = heapq.heappop(prior_queue)

            if best_visited[node] <= steps:
                continue

            if steps>K:  # More than k stops, invalid
                continue

            if node==dst:
                return cost

            best_visited[node] = steps #Update steps

            for neighb, weight in adj_list[node]:
                if steps + 1 < best_visited[neighb]: #Push neighb into the heap, only if steps+1 is
                    heapq.heappush(prior_queue, (cost+weight, steps + 1, neighb))

        return -1

n=3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0

#n=11
#flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
#src = 0
#dst = 2
#K = 4

print(Solution().findCheapestPrice(n, flights, src, dst, K))




# adj_list = defaultdict(list)
# for u, v, w in flights:
#     adj_list[u].append((v,w))
#
# best_visited = defaultdict(lambda : 'Inf')
#
# prior_queue = [ (0, -1, src) ] #weight, steps, node
#
# while prior_queue:
#     cost, steps, node = heapq.heappop(prior_queue)
#
#     if best_visited[node] <= steps:
#         continue
#
#     if steps>k:  # More than k stops, invalid
#         continue
#
#     if node==dst:
#         return cost
#
#     best_visited[node] = steps #Update steps
#
#     for neighb, weight in adj_list[node]:
#         if steps + 1 < best_visited[neighb]: #Push neighb into the heap, only if steps+1 is
#             heapq.heappush(prior_queue, (cost+weight, steps + 1, neighb))
#
# return -1


# Build the adjacency matrix
# adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
# for s, d, w in flights:
#     adj_matrix[s][d] = w
#
# # Shortest distances array
# distances = [float("inf") for _ in range(n)]
# current_stops = [float("inf") for _ in range(n)]
# distances[src], current_stops[src] = 0, 0
#
# # Data is (cost, stops, node)
# minHeap = [(0, 0, src)]
#
# while minHeap:
#
#     cost, stops, node = heapq.heappop(minHeap)
#
#     # If destination is reached, return the cost to get here
#     if node == dst:
#         return cost
#
#     # If there are no more steps left, continue
#     if stops == K + 1:
#         continue
#
#     # Examine and relax all neighboring edges if possible
#     for nei in range(n):
#         if adj_matrix[node][nei] > 0:
#             dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
#
#             # Better cost?
#             if dU + wUV < dV:
#                 distances[nei] = dU + wUV
#                 heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
#             elif stops < current_stops[nei]:
#
#                 #  Better steps?
#                 current_stops[nei] = stops
#                 heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
#
# return -1 if distances[dst] == float("inf") else distances[dst]

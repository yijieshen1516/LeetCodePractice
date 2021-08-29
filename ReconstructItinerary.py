from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        """"
        graph backtracking problem
        backtracking only needs one answer, so stopped after getting one answer
        """

        self.graph = defaultdict(list)

        for ticket in tickets:
            self.graph[ticket[0]].append(ticket[1])

        self.length = len(tickets)
        self.visited = defaultdict(list)

        for origin, ticket in self.graph.items():
            ticket.sort()
            self.visited[origin] = [False]* len(ticket)

        route = ['JFK']
        self.results = []

        self.helper('JFK', route)

        return self.results

    def helper(self, node, route):

        if len(route) == self.length +1:
            self.results = route[:]
            return True

        for idx, nei in enumerate(self.graph[node]):
            if not self.visited[node][idx]:
                self.visited[node][idx] = True
                route.append(nei)
                found = self.helper(nei, route)
                if found:
                    return found
                route.pop()
                self.visited[node][idx] = False


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution().findItinerary(tickets))



# from collections import defaultdict
# self.flightMap = defaultdict(list)
#
# for ticket in tickets:
#     start, end = ticket[0], ticket[1]
#     self.flightMap[start].append(end)
#
# for origin, itin in self.flightMap.items():
#     itin.sort()
#
# startName = 'JFK'
# self.res = []
# self.helper(startName)
#
# return self.res
#
# def helper(self, startName):
#     itin = self.flightMap[startName]
#
#
#     while itin:
#         name = itin[0]
#         itin.pop(0)
#         self.helper(name)
#
#     self.res.append(startName)
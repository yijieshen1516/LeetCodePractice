class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            start, end = ticket[0], ticket[1]
            self.flightMap[start].append(end)

        for origin, itin in self.flightMap.items():
            itin.sort()

        startName = 'JFK'
        self.res = []
        self.helper(startName)

        return self.res

    def helper(self, startName):
        itin = self.flightMap[startName]


        while itin:
            name = itin[0]
            itin.pop(0)
            self.helper(name)

        self.res.append(startName)

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))
import collections

class Solution(object):
    def accountsMerge(self, accounts):
        # draw an edge between two emails if they occur in the same account
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        visited = set()
        ans = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)

                ans.append([em_to_name[email]] + sorted(component))

        return ans


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(Solution().accountsMerge(accounts))


#build graph with key email and list as connected emails
#dfs each key

# self.em_to_name = {}
# self.graph = collections.defaultdict(set)
# for acc in accounts:
#     name = acc[0]
#     for email in acc[1:]:
#         self.graph[acc[1]].add(email)
#         self.graph[email].add(acc[1])
#         self.em_to_name[email] = name
#
# self.visited = set()
# ans = []
#
# for email in self.graph:
#     self.res = []
#     if email not in self.visited:
#         self.res.append(email)
#         self.visited.add(email)
#         self.helper(email)
#
#         ans.append([self.em_to_name[email]] + sorted(self.res))
#
# return ans
#
#
# def helper(self, node):
#
#     for nei in self.graph[node]:
#         if nei not in self.visited:
#             self.visited.add(nei)
#             self.res.append(nei)
#             self.helper(nei)

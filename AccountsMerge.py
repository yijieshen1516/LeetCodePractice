import collections

class Solution(object):
    def accountsMerge(self, accounts):
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




        return graph


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(Solution().accountsMerge(accounts))
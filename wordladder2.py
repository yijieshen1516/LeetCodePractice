#from collections import deque
#from collections import defaultdict
import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]

        all_combo_dict= defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                all_combo_dict[word[:idx] + "*" + word[idx+1:]].append(word)

        res = self.bfs(beginWord, endWord, all_combo_dict)

        return res


    def bfs(self, beginWord, endWord, all_combo_dict):

        queue = deque([(beginWord, [beginWord])])
        visited = set()
        visited.add(beginWord)
        res = []
        while queue:
            length = len(queue)
            localVisited = set()

            for _ in range(length):
                word, path = queue.popleft()

                for idx in range(len(word)):
                    tmp_word = word[:idx] + "*" + word[idx+1:]
                    for middle_word in all_combo_dict[tmp_word]:

                        if middle_word in visited:
                            continue

                        if middle_word == endWord:
                            path.append(endWord)
                            res.append(path[:])

                        localVisited.add(middle_word)
                        queue.append((middle_word, path + [middle_word]))
            visited = visited.union(localVisited)

        return res
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        print(all_combo_dict)
        # Build graph, BFS
        # ans = []
        queue = collections.deque()
        queue.append(beginWord)
        parents = collections.defaultdict(set)
        visited = set([beginWord])
        found = False
        depth = 0
        while queue and not found:
            depth += 1
            length = len(queue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == word:
                            continue
                        if nextWord not in visited:
                            parents[nextWord].add(word)
                            if nextWord == endWord:
                                found = True
                            localVisited.add(nextWord)
                            queue.append(nextWord)
            visited = visited.union(localVisited)

        print(parents)
        # Search path, DFS
        ans = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    ans.append(path[::-1])
                return
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d-1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans

#beginWord = "a"
#endWord = "c"
#wordList = ["a", "b", "c"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
#wordList = ["hot", "dot", "dog", "lot", "log"]
print(Solution().findLadders(beginWord, endWord, wordList))
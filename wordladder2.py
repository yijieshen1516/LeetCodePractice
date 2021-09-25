from collections import deque
from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

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
            word, path = queue.popleft()

            for idx in range(len(word)):
                tmp_word = word[:idx] + "*" + word[idx+1:]
                for middle_word in all_combo_dict[tmp_word]:
                    if middle_word == endWord:
                        path.append(endWord)
                        res.append(path[:])
                    elif middle_word not in visited:
                        visited.add(middle_word)
                        queue.append((middle_word, path + [middle_word]))
        return res


beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
#wordList = ["hot", "dot", "dog", "lot", "log"]
print(Solution().findLadders(beginWord, endWord, wordList))
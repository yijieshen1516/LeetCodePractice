from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        all_combo_dict= defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        res = self.bfs(beginWord, endWord, all_combo_dict)

        return res

    def bfs(self, beginWord, endWord, all_combo_dict):

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                tmp_word = word[:i] + "*" + word[i+1:]
                for middle_word in all_combo_dict[tmp_word]:
                    if middle_word == endWord:
                        return level + 1
                    if middle_word not in visited:
                        visited.add(middle_word)
                        queue.append((middle_word, level+1))


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
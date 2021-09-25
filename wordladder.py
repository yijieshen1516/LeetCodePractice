from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

    #     all_combo_dict= defaultdict(list)
    #     for word in wordList:
    #         for i in range(len(word)):
    #             all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    #
    #     res = self.bfs(beginWord, endWord, all_combo_dict)
    #
    #     return res
    #
    # def bfs(self, beginWord, endWord, all_combo_dict):
    #
    #     queue = deque([(beginWord, 1)])
    #     visited = set()
    #     visited.add(beginWord)
    #     while queue:
    #         word, level = queue.popleft()
    #         for i in range(len(word)):
    #             tmp_word = word[:i] + "*" + word[i+1:]
    #             for middle_word in all_combo_dict[tmp_word]:
    #                 if middle_word == endWord:
    #                     return level + 1
    #                 if middle_word not in visited:
    #                     visited.add(middle_word)
    #                     queue.append((middle_word, level+1))


        queue = [(beginWord, 1)]
        wordList = set(wordList) # here set in time is o(1), in list time is o(n)
        while queue:

            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append((next_word, length+1))


        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
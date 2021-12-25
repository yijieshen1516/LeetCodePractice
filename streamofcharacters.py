from collections import deque

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
obj = StreamChecker(["cd", "f", "kl"])
print(obj.query('a'))
print(obj.query('b'))
print(obj.query('c'))
print(obj.query('d'))
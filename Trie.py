class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch == '.':
                        for x in node:
                            if x!= '$' and search_in_node(word[i+1:], node[x]):
                                return True
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
#param_2 = obj.search(word)
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        self.dict_map = {}

        for idx, s in enumerate(order):
            self.dict_map[s] = idx

        for idx in range(1, len(words)):
            if not self.compare(words[idx - 1], words[idx]):
                return False

        return True

    def compare(self, word1, word2):

        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            tmp1 = self.dict_map[word1[i]]
            tmp2 = self.dict_map[word2[j]]

            if tmp1 < tmp2:
                return True
            elif tmp1 > tmp2:
                return False

            i += 1
            j += 1

        if i < len(word1):
            return False

        if j < len(word2):
            return True


words = ['word', 'world', 'row']
order = 'worldabcefghijkmnpqstuvxyz'

print(Solution().isAlienSorted(words, order))

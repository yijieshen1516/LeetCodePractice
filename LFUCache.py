from collections import defaultdict
from collections import OrderedDict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.freq_bins = defaultdict(OrderedDict)
        self.min_freq = 0
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1

        val, freq = self.table[key]
        self.table[key] = val, freq + 1

        freq_bin = self.freq_bins[freq]
        del freq_bin[key]

        next_freq_bin = self.freq_bins[freq + 1]
        next_freq_bin[key] = True
        self.freq_bins[freq+1] = next_freq_bin

        if len(freq_bin) == 0 and freq == self.min_freq:
            self.min_freq = freq+1

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.capacity == 0:
            return

        if key in self.table:
            val, freq = self.table[key]
            self.table[key] = (value, freq+1)

            freq_bin = self.freq_bins[freq]
            del freq_bin[key]

            next_freq_bin = self.freq_bins[freq+1]
            next_freq_bin[key] = True
            self.freq_bins[freq+1] = next_freq_bin

            if len(freq_bin) == 0 and freq == self.min_freq:
                self.min_freq = freq+1

            return

        if self.count == self.capacity:
            freq_bin = self.freq_bins[self.min_freq]
            k, _ = freq_bin.popitem(last=False)
            del self.table[k]
            self.count -= 1

        self.table[key] = (value, 1)
        self.count += 1
        freq_bin = self.freq_bins[1]
        freq_bin[key] = True
        self.freq_bins[1] = freq_bin
        self.min_freq = 1
        return


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))
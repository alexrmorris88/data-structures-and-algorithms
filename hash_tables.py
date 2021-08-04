# =============================================================================
# Hash Table - Without Collisions
# =============================================================================


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.array[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.array[h] = None


# if __name__ == "__main__":
#     hashtable = HashTable()
#     hashtable['March 6'] = 227
#     hashtable['March 7'] = 333
#     hashtable['March 8'] = 4644
#     hashtable['March 9'] = 29902
#
#     del hashtable['March 9']
#
#     print(hashtable.array)


# =============================================================================
# Hash Table - With Collisions
# =============================================================================

class HashTable:
    def __init__(self):
        self.max_len = 10
        self.max_depth = 10
        self.array = [[] for i in range(self.max_len)]  # Add in a list within a list

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max_len

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for index, element in enumerate(self.array[h]):
            if len(element) == self.max_depth and element[0] == key:
                self.array[h][index] = (key, value)
                found = True
                break

        if not found:
            self.array[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][index]


if __name__ == "__main__":
    h = HashTable()
    h['March 1'] = 111
    h['March 1'] = 112
    h['March 1'] = 113
    h['March 11'] = 113
    h['March 2'] = 222
    h['March 3'] = 333
    h['March 4'] = 444
    h['March 6'] = 555
    h['March 6'] = 666
    print(h.array)

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


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable['March 6'] = 227
    hashtable['March 7'] = 333
    hashtable['March 8'] = 4644
    hashtable['March 9'] = 29902

    del hashtable['March 9']

    print(hashtable.array)
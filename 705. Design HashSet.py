class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 4
        self.mp = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
    
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        bucket = self.mp[self._hash(key)]
        bucket.append(key)

    def remove(self, key: int) -> None:
        i = self._hash(key)
        bucket = self.mp[i]
        self.mp[i] = [val for val in bucket if val != key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self.mp[self._hash(key)]
        return key in bucket

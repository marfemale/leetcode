class Node:
    def __init__(self, key, val, node = None):
        self.key = key
        self.val = val
        self.next = node
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.mp = [Node(-1, -1) for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        cur_node = self.mp[self._hash(key)]
        while cur_node:
            if cur_node.key == key:
                cur_node.val = value
                return
            pre = cur_node
            cur_node = cur_node.next
        pre.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        cur_node = self.mp[self._hash(key)]
        while cur_node:
            if cur_node.key == key:
                return cur_node.val
            cur_node = cur_node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pre = self.mp[self._hash(key)]
        cur_node = pre.next
        while cur_node:
            if cur_node.key == key:
                nxt = cur_node.next
                pre.next = nxt
                return
            pre = cur_node
            cur_node = cur_node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None
        
class Skiplist:
    def __init__(self):
        self.levels = []
        pre = None
        for _ in range(16):
            node = Node(-inf)
            self.levels.append(node)
            if pre:
                pre.down = node
            pre = node
            
    def _iter(self, val):
        res = []
        last = self.levels[0]
        while last:
            while last.next and last.next.val < val:
                last = last.next
            res.append(last)
            last = last.down
        return res

    def search(self, target: int) -> bool:
        last = self._iter(target)[-1]
        return last.next and last.next.val == target

    def add(self, num: int) -> None:
        res = self._iter(num)
        pre = None
        for i in range(len(res) - 1, -1, -1):
            node = Node(num)
            node.next, node.down = res[i].next, pre
            res[i].next = node
            pre = node
            rand = random.random()
            if rand > 0.5:
                break    

    def erase(self, num: int) -> bool:
        found = False
        res = self._iter(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.val == num:
                res[i].next = res[i].next.next
                found = True
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.arr = [0] * m
        self.lh1, self.rh1 = self.heap_init(m, k)
        self.lh2, self.rh2 = self.heap_init(m, m - k)
        self.res = 0
        
    def heap_init(self, p1, p2):
        h1 = [(0, i) for i in range(p1 - p2, p1)]
        h2 = [(0, i) for i in range(p1 - p2)]
        heapq.heapify(h1)
        heapq.heapify(h2)
        return (h1, h2)
    
    def update(self, lh, rh, m, k, num):
        res, T = 0, len(self.arr)
        if num > rh[0][0]:
            heapq.heappush(rh, (num, T))
            if self.arr[T - m] <= rh[0][0]:
                if rh[0][1] >= T - m:
                    res += rh[0][0]
                res -= self.arr[T - m]
                heapq.heappush(lh, (-rh[0][0], rh[0][1]))
                heapq.heappop(rh)
        else:
            heapq.heappush(lh, (-num, T))
            res += num
            if self.arr[T - m] >= rh[0][0]:
                heapq.heappush(rh, (-lh[0][0], lh[0][1]))
                q = heapq.heappop(lh)
                res += q[0]
            else:
                res -= self.arr[T - m]
        while lh and lh[0][1] <= T - m:
            heapq.heappop(lh)
        while rh and rh[0][1] <= T - m:
            heapq.heappop(rh)
        return res

    def addElement(self, num: int) -> None:
        t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
        t2 = self.update(self.lh2, self.rh2, self.m, self.m - self.k, num)
        self.arr.append(num)
        self.res += (t2 - t1)

    def calculateMKAverage(self) -> int:
        if len(self.arr) < 2 * self.m: return -1
        return self.res // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

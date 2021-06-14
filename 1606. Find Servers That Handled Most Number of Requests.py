class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        times = [0] * k
        ava, use = [i for i in range(k)], []
        heapq.heapify(ava)
        for i in range(len(load)):
            while use and use[0][0] <= arrival[i]:
                _, s = heapq.heappop(use)
                heapq.heappush(ava, i + (s - i) % k)
            if ava:
                j = heapq.heappop(ava)
                times[j % k] += 1
                heapq.heappush(use, (arrival[i] + load[i], j % k))
        maxq = max(times)
        return [i for i in range(k) if times[i] == maxq]

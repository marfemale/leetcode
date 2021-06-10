class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        hq, left, right, res = [], inf, 0, inf
        for num in nums:
            if num % 2:
                num = num * 2
            heapq.heappush(hq, -num)
            left = min(left, num)
        while True:
            right = -heapq.heappop(hq)
            if right - left < res:
                res = right - left
            if right % 2 == 0:
                heapq.heappush(hq, -right // 2)
                left = min(left, right // 2)
            else:
                break
        return res

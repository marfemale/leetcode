class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hq, right = [], -inf
        for i, row in enumerate(nums):
            heapq.heappush(hq, (row[0], i, 0))
            right = max(right, row[0])
        res = [-inf, inf]
        while True:
            left, i, j = heapq.heappop(hq)
            if right - left < res[1] - res[0]:
                res = [left, right]
            if j + 1 == len(nums[i]):
                return res
            nxt = nums[i][j + 1]
            right = max(right, nxt)
            heapq.heappush(hq, (nxt, i, j + 1))

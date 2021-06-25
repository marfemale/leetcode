class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # pos = defaultdict(list)
        # for i, num in enumerate(nums):
        #     pos[num].append(i)
        # res = []
        # for l, r in queries:
        #     pre, diff = 0, inf
        #     for i in range(1, 101):
        #         if not pos[i]:
        #             continue
        #         s = bisect.bisect_left(pos[i], l)
        #         e = bisect.bisect(pos[i], r)
        #         if s == e:
        #             continue
        #         if pre:
        #             diff = min(diff, i - pre)
        #             if diff == 1:
        #                 break
        #         pre = i
        #     res.append(diff if diff < inf else -1)
        # return res
        maxnum = max(nums)
        presum = [[0] * (maxnum + 1)]
        for num in nums:
            cur = presum[-1][:]
            cur[num] += 1
            presum.append(cur)
        res = []
        for l, r in queries:
            pre, diff = 0, inf
            for i in range(1, maxnum + 1):
                cnt = presum[r + 1][i] - presum[l][i]
                if cnt:
                    if pre:
                        diff = min(diff, i - pre)
                        if diff == 1:
                            break
                    pre = i
            res.append(diff if diff < inf else -1)
        return res

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def check(x):
            res, anchor = 1, position[0]
            for num in position:
                if num >= anchor + x:
                    res += 1
                    anchor = num
            return res
        left, right = 0, position[-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid) < m:
                right = mid - 1
            else:
                left = mid + 1
        return right

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def check(x):
            res = 0
            for num in arr:
                if num < x:
                    res += num
                else:
                    res += x
            return res
        left, right = 0, max(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid) == target:
                return mid
            elif check(mid) < target:
                left = mid
            else:
                right = mid
        if abs(check(left) - target) <= abs(check(right) - target):
            return left
        else:
            return right

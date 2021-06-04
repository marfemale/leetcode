class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def check(x):
            res = 0
            if x > index:
                res += (2 * x - index) * (index + 1) // 2
            else:
                res += x * (x + 1) // 2
            if x >= n - index:
                res += (2 * x - n + index + 1) * (n - index) // 2
            else:
                res += x * (x + 1) // 2
            return res - x
        maxSum -= n
        left, right = 0, maxSum
        while left <= right:
            mid = (left + right) // 2
            if check(mid) > maxSum:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

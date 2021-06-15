class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        nums.append(0)
        res, stack = 0, [-1]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                minval = nums[stack.pop()]
                cursum = presum[i] - presum[stack[-1] + 1]
                res = max(res, minval * cursum)
            stack.append(i)
        return res

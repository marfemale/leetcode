class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack, res = [], 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                res += i - stack.pop()
            stack.append(i)
        n = len(nums)
        while stack:
            res += n - stack.pop()
        return res

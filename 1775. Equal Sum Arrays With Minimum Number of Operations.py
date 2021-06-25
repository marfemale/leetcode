class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1
        c1, c2 = Counter(nums1), Counter(nums2)
        res = 0
        for i in range(5):
            cnt = c1[i + 1] + c2[6 - i]
            if cnt * (5 - i) >= diff:
                res += math.ceil(diff/ (5 - i))
                diff = 0
                break
            else:
                res += cnt
                diff -= cnt * (5 - i)
        return res if not diff else -1

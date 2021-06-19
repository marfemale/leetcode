class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score, pos, res = 0, {}, 0
        for i in range(len(hours)):
            score = score + 1 if hours[i] > 8 else score - 1
            if score > 0:
                res = i + 1
            if score - 1 in pos:
                res = max(res, i - pos[score - 1])
            if score not in pos:
                pos[score] = i
        return res

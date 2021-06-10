class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        val = sum(row[0] for row in mat)
        pq = [(val, [0] * m, 0)]
        for _ in range(k):
            val, idx, cur_r = heapq.heappop(pq)
            for i in range(cur_r, m):
                nidx = list(idx)
                if nidx[i] +1 == n:
                    continue
                nidx[i] += 1
                newval = val - mat[i][idx[i]] + mat[i][nidx[i]]
                heapq.heappush(pq, (newval, nidx, i))
        return val

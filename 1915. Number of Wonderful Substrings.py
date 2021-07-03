class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        c = [1] + [0] * 1024
        res, cur = 0, 0
        #[1,1,0,1,0,0....]
        #cur = 1 res = 1
        #cur = 3 res = 2
        for ch in word:
            cur ^= 1 << (ord(ch) - ord("a"))
            #no odd number of times
            res += c[cur]
            for i in range(10):
                cur ^= 1 << i
                #one odd number of times
                res += c[cur]
                cur ^= 1 << i
            c[cur] += 1
        return res

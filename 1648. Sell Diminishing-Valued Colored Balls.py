class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse = True)
        inventory.append(0)
        res, k, mod = 0, 1, 10 ** 9 + 7
        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                if k * (inventory[i] - inventory[i + 1]) < orders:
                    res += k * (inventory[i] + inventory[i + 1] + 1) * (inventory[i] - inventory[i + 1] ) // 2
                    orders -= k * (inventory[i] - inventory[i + 1])
                else:
                    q, r = orders // k, orders % k
                    res += k * (2 * inventory[i] - q + 1) * q // 2 + r * (inventory[i] - q)
                    return res % mod
                res %= mod
            k += 1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(piles, k, hours):
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            return True if res <= hours else False





        l, r = 1, max(piles)

        res = math.inf
        while l <= r:
            m = l + (r - l) // 2
            
            if canEat(piles.copy(), m, h):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

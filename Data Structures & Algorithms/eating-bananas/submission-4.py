class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(piles, rate, h): #[0,0,0,1]  rate = 1  h = 0  curr = 3
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / rate)
            
            if time_taken <= h:
                return True
            return False

        l, r = 1, max(piles)

        res = math.inf
        while l <= r:
            mid = l + (r - l) // 2
            if canEat(piles.copy(), mid, h):
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        return res
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min is number of piles
        # max is the max pile size
        # [1,2,3,4,20] h=5, res=20
        # [1,2,3,4,20] h=6, res=10
        # [1,2,3,4,20] h=7, res=7
        # [1,2,3,15,20] h=6, res=
        total_bananas = sum(piles)
        def countHours(speed: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            # print(hours)
            return hours

        

        lo = total_bananas // h
        hi = max(piles)
        # print(lo, hi)
        speed = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid <= 0:
                return speed
            if countHours(mid) < h:
                speed = min(speed, mid)
                hi = mid - 1
            elif countHours(mid) > h:
                lo = mid + 1
            else:
                speed = min(speed, mid)
                hi = mid - 1
        return speed
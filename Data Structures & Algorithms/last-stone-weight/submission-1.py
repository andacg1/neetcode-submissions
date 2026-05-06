from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            first_stone = heappop_max(stones)
            second_stone = heappop_max(stones)
            if first_stone == second_stone:
                continue
            heappush_max(stones, abs(first_stone - second_stone))
        if len(stones) == 0:
            return 0
        return stones[0]
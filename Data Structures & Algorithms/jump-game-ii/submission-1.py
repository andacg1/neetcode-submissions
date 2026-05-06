from math import *
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        can_reach = nums[0]
        # [4,10,1,1,20,1,1,1,...,1]
        best_jumps = [inf] * len(nums)
        for i in range(len(nums)):
            n = nums[i]
            for j in range(i, min(i + n, len(nums) - 1) + 1):
                best_jumps[j] = min(best_jumps[j], i)
        i = len(nums) - 1
        print(best_jumps)
        while i > 0:
            i = best_jumps[i]
            jumps += 1
        return jumps
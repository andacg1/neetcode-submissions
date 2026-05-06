class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = nums[0]
        for n in nums[1:]:
            fuel -= 1
            if fuel < 0:
                return False
            fuel = max(n, fuel)
        if fuel < 0:
            return False
        return True
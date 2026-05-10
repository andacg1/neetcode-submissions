class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        memo[0] = nums[0]
        memo[1] = nums[1]
        for i in range(2, len(nums)):
            prev = memo[i - 1]
            two_prev = memo[i - 2]
            if i < 3:
                memo[i] = nums[i] + memo[i - 2]
            else:
                memo[i] = nums[i] + max(memo[i - 2], memo[i - 3])
        return max(memo[-1], memo[-2])
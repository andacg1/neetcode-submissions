class Solution:
    def rob(self, nums: List[int]) -> int:
        next_i = lambda i: (i + 1) % len(nums)
        memo = [0] * len(nums)
        if len(nums) <= 3:
            return max(nums)
        memo[0] = nums[0]
        memo[1] = nums[1]
        for i in range(2, len(nums) - 1):
            memo[i] = max(memo[i - 2], memo[i - 3]) + nums[i]
        start_first = max(memo[-2], memo[-3])
        memo[0] = 0
        memo[1] = nums[1]
        for i in range(2, len(nums)):
            memo[i] = max(memo[i - 2], memo[i - 3]) + nums[i]
        start_second = max(memo[-1], memo[-2])
        return max(start_first, start_second)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = nums[0]
        for num in nums[1:]:
            curr = (curr) ^ (num)
        return curr
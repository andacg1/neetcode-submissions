class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)
        # nums = deque(nums)
        if len(nums) == 1:
            return nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(mid)
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[-1]:
                lo = mid + 1
            elif nums[mid] < nums[0]:
                hi = mid - 1
            else:
                # print("else")
                hi = mid - 1
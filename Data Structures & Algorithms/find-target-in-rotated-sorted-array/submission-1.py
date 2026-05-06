class Solution:
    def binarySearch(self, nums: List[int], target: int, lo: int, hi: int) -> int:

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        pivot = 0
        # find pivot
        # if len(nums) <= 6:
        #     try:
        #         return nums.index(target)
        #     except:
        #         return -1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(mid)
            if nums[mid] < nums[mid - 1]:
                right_val = nums[mid + 1] if mid < len(nums) - 1 else nums[0]
                if nums[mid] < right_val:
                    pivot = mid
                break
            if nums[-1] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        # print(nums[pivot])
        if nums[pivot] == target:
            return pivot
        lo = 0
        hi = pivot - 1
        return max(
            -1,
            self.binarySearch(nums, target, 0, pivot - 1),
            self.binarySearch(nums, target, pivot + 1, len(nums) - 1)
            )
        
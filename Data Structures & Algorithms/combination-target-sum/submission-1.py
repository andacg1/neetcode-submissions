class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combs = []
        # candidates.sort()
        def traverse(nums: List[int], start: int, curr_sum: int):
            if curr_sum == target:
                all_combs.append(nums.copy())
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                nums.append(candidate)
                traverse(nums, i, curr_sum + candidate)
                nums.pop()
        traverse([], 0, 0)
        return all_combs
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total_num = 2 ** (len(nums))
        all_sets = []
        for i in range(total_num):
            temp_set = []
            for sh in range(len(nums)):
                mask = 1 << sh
                if mask & i:
                    temp_set.append(nums[sh])
            all_sets.append(temp_set)
        return all_sets
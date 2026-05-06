class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        def traverse(candidate: List[int], start: int, curr_sum: int):
            if curr_sum == target:
                result.add(tuple(candidate))
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                candidate.append(candidates[i])
                traverse(candidate, i + 1, curr_sum + candidates[i])
                candidate.pop()
        traverse([], 0, 0)
        return list(map(list, result))
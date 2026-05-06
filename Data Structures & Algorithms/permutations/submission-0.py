class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def traverse(candidate: List[int], remaining: Set[int]):
            if len(candidate) == len(nums):
                result.append(list(candidate))
                return
            for n in list(remaining):
                candidate.append(n)
                remaining.remove(n)
                traverse(candidate, remaining)
                remaining.add(n)
                candidate.pop()
        traverse([], set(nums))
        return result
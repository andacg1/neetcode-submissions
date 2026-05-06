class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            anagram = "".join(sorted(list(s)))
            if anagram not in result.keys():
                result[anagram] = []
            result[anagram].append(s)
        return list(result.values())
            
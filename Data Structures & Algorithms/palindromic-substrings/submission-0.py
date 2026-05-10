class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            single_letter = left == right
            count = 0
            # print(f"left:{left}, right:{right}")
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    # print(s[left:right + 1])
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
            # print(s[left:right + 1], count)
            return count
        total_count = 0
        for i in range(len(s)):
            if not (i == 0):
                total_count += expand(i - 1, i)
            total_count += expand(i, i)
        return total_count

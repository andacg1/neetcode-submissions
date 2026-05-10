class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def expand(left: int, right: int) -> Tuple[int, str, bool]:
            is_palindrome = True
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    is_palindrome = False
                    break
            # print(right, left)
            right -= 1
            left += 1
            return (right - left + 1, s[left:right + 1], is_palindrome)
        max_len = 1
        memo = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                memo.append(expand(i - 1, i))
            memo.append(expand(i, i))
        return max(memo)[1]
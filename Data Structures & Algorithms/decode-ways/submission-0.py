class Solution:
    def numDecodings(self, s: str) -> int:
        valid_codes = {str(num) for num in range(1, 27)}

        def is_valid(code: str) -> bool:
            return code in valid_codes
        memo = [0] * len(s)
        if is_valid(s[0]):
            memo[0] = 1
        if len(s) <= 1:
            return memo[0]
        if is_valid(s[:2]):
            memo[1] += 1
        if is_valid(s[1:2]):
            memo[1] += memo[0]
        # print(memo)
        for i in range(2, len(s)):
            if i == 0:
                if is_valid(s[i]):
                    memo[i] = 1
                continue
            # print(s[i - 1:i + 1], s[i:i+1])
            if is_valid(s[i - 1:i + 1]):
                memo[i] += memo[i - 2]
            if is_valid(s[i:i + 1]):
                memo[i] += memo[i - 1]
        # print(memo)
        return memo[-1]
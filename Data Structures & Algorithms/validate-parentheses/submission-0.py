class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(','{','['])
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for char in s:
            if len(stack) == 0:
                if char in pairs:
                    stack.append(char)
                else:
                    return False
                continue
            if char in pairs:
                stack.append(char)
            elif pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return len(stack) == 0
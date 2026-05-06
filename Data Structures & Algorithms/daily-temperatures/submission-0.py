class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            # print(i)
            # print(stack)
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack) > 0:
                # print(stack)
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
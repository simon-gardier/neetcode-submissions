class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            if len(stack) == 0 or stack[-1][1] >= temperature:
                stack.append((i, temperature))
            else:
                while len(stack) and stack[-1][1] < temperature:
                    j, smaller_temp = stack.pop()
                    results[j] = i - j
                stack.append((i, temperature))
        return results

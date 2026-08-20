class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                j, smaller_temp = stack.pop()
                results[j] = i - j
            stack.append((i, temperature))
        return results

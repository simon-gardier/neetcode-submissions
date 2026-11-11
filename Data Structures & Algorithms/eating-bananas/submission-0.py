class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        solution = right

        while left <= right:
            middle = (left + right) // 2
            hours_passed = 0
            for pile in piles:
                hours_passed += -(-pile // middle)
                if hours_passed > h:
                    left = middle + 1
                    break

            if hours_passed <= h:
                solution = min(solution, middle)
                right = middle - 1
        return solution

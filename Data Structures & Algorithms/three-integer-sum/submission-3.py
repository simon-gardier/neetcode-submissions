class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        current, left, right = 0, 1, len(nums) - 1
        nums.sort()

        while current < len(nums) - 2 and nums[current] < 1:
            if (current >= 1 and nums[current] == nums[current-1]):
                current += 1
                continue
            left = current + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[current] == 0:
                    sol.append([nums[current], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                if nums[left] + nums[right] + nums[current] > 0:
                    right -= 1
                if nums[left] + nums[right] + nums[current] < 0:
                    left += 1
            current += 1
        return sol

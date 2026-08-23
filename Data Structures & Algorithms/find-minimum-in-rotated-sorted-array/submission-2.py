class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2
        min_value = math.inf
        while left <= right:
            min_value = min(min_value, nums[middle])
            if nums[left] <= nums[middle] <= nums[right]:
                return min(min_value, nums[left])
            if nums[left] <= nums[middle]:
                left = middle + 1
                middle = left + (right - left) // 2
            else:
                right = middle - 1
                middle = left + (right - left) // 2

        return min_value

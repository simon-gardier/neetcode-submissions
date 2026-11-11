class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if (nums[middle] == target):
                res = middle
                break
            # left sorted
            elif nums[middle] >= nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            # right sorted
            else:
                if target > nums[right] or target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return res
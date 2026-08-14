class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j  in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [None, None]

        numbers_occurences = {}
        for i, x in enumerate(nums):
            pair_x = target - x
            if numbers_occurences.get(pair_x) is not None:
                return [numbers_occurences[pair_x], i]
            else:
                numbers_occurences[x] = i
        return [None, None]

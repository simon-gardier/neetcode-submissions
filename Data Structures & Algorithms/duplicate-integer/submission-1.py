class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyPresents = set()
        for x in nums:
            if x in alreadyPresents:
                return True
            alreadyPresents.add(x)
        return False

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i]:
        #         return True
        # return False

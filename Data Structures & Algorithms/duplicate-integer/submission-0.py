class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyPresents = {}
        for x in nums:
            if x in alreadyPresents:
                return True
            alreadyPresents[x] = True
        return False

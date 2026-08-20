class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)

        curr_prefix_product = 1
        curr_suffix_product = 1
        for i in range(0, len(nums)):
            prefix_products[i] = curr_prefix_product
            suffix_products[len(nums) - 1 - i] = curr_suffix_product
            
            curr_prefix_product *= nums[i]
            curr_suffix_product *= nums[len(nums) - 1 - i]

        products = [0] * len(nums)
        for i in range(len(nums)):
            products[i] = prefix_products[i] * suffix_products[i]
        
        return products

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Correct Prefix Product Calculation
        prefix_product = [1] * n  # Initialize the prefix product array
        prefix = 1  # Variable to store the running product from the left
        for i in range(n):
            prefix_product[i] = prefix  # Store the product of all elements before nums[i]
            prefix *= nums[i]  # Update the prefix with the current element
        
        suffix_product = [1] * n 
        suffix = 1  # Variable to store the running product from the right
        for i in range(n - 1, -1, -1):  # Iterate from right to left
            suffix_product[i] = suffix  
            suffix *= nums[i] 

        result = []
        for i in range(n):
            res = prefix_product[i] * suffix_product[i]  # Multiply the prefix and suffix
            result.append(res)

        return result

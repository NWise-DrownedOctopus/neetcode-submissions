class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        # First lets calaculate our prefix product values
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # Second lets calculate our postfix product values
        postfix = 1
        # Start at end of array, end once we pass 0, go down by 1 each cycle
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

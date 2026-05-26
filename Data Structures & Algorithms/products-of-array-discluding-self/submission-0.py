class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        i = 0
        # I want to run the loop once for each number in the list
        while i < len(nums):
            # We initilize the entry with 1 to start
            entry = 1
            # Now we want to go through the whole list and multiply each entry, except for the current position
            n = 0
            while n < len(nums):
                if n == i:
                    n += 1
                    continue
                entry *= nums[n]
                n += 1

            # Here we add the entry to the arry, and move to the next entry
            result.append(entry)
            i += 1

        return result
            
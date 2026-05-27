class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first lets convert our list into a set, so we ignore any duplicates
        num_set = set(nums)

        # We can also set our starting sequnce value to 0
        max_length = 0

        # To start tracking a sequnce we need to identify if it has a left neighbor, if not, we know that it is the start of a sequnce
        for num in num_set:
            if (num - 1) not in num_set:
                length = 0
                # Here we know that the number is a sequnce starter, so lets find how far it goes
                # If we can find the next number we add to the length until we can't find another
                while (num + length) in num_set:
                    length += 1                
                # now lets check if this length is greater than our current max
                max_length = max(max_length, length)

        # Now just return our maximum length we found
        return max_length
        


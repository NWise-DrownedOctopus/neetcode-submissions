class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        second_index = 1

        while first_index < len(nums):
            if nums[first_index] + nums[second_index] == target:
                return [first_index, second_index]
            else:
                second_index += 1

                if second_index == len(nums):
                    first_index += 1
                    second_index = first_index + 1
                    continue

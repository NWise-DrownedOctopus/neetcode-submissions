class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set(())
        for num in nums:
            newSet.add(num)
        
        if len(newSet) != len(nums):
            return True
        
        return False
        
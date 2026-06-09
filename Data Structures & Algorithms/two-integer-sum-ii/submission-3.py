class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = 0
        m = 1

        while n < len(numbers):
            while m < len(numbers):
                sum = numbers[n] + numbers[m]
                if sum == target:
                    return [n + 1, m + 1]
                elif sum > target:
                    break
                m += 1
            n += 1
            m = n + 1
            

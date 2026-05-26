class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First I'll generate a dictionary that acts as a hashMap, we will store each unique number with it's frrequency
        hashMap = {}
        # For each number, check if it's a key, if so increment value, otherwise generate new key and set value to 1
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1

        # I now have a dictionary where each key is a unique number from the origianl list, and each value is it's frequncy in that list
        
        # Now I will find which entry has the highest frequency for as many times as k equals
        output = []
        i = 0
        while i < k:
            # We set the max to the first key in the dict
            max = next(iter(hashMap))
            for num in hashMap:
                if hashMap[num] > hashMap[max]:
                    max = num
            output.append(max)
            hashMap.pop(max)
            i += 1
        return output
            
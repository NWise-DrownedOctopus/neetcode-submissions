class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # We want to create a hashmap for each string, we could store them all in an array for now, and then we can move
        # to sorting them if they are equal. We need to maintain a refernce to the origianl string as well however, so lets make them 
        # touples for now
        hashed_strs = []
        for string in strs:
            hash = {}
            for char in string:
                if char not in hash:
                    hash[char] = 1
                else:
                    hash[char] += 1
            hashed_strs.append([hash, string])
        
        # Now that they are converted to hash maps we need to find which ones are equivalent and then some how group them together
        # I think we can start with first entry, remove it from the array, and then check each other entry and put them in a list that we
        # can then add to a fianl array for output
        output = []
        while len(hashed_strs) > 0:
            anagrams = []
            anagram = hashed_strs.pop(0)
            anagrams.append(anagram[1])
            i = 0
            while i < len(hashed_strs):
                if hashed_strs[i][0] == anagram[0]:
                    anagrams.append(hashed_strs[i][1])
                    hashed_strs.pop(i)
                else:
                    i += 1
            output.append(anagrams)

        return output
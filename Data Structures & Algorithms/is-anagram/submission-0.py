class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMapS = {}
        for letter in s:
            if letter not in countMapS:
                countMapS[letter] = 1   
            else:
                countMapS[letter] += 1

        countMapT = {}
        for letter in t:
            if letter not in countMapT:
                countMapT[letter] = 1
            else:
                countMapT[letter] += 1

        if countMapS == countMapT:
            return True
        else:
            return False
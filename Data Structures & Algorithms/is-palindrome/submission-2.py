class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        front_index = 0
        back_index = len(s) - 1

        # We want to compair our front char and our back char until our index meets in the middle
        
        # We should enter our main loop, we can leave when our indices aren't the same

        while front_index != back_index and front_index < back_index:
            # First we need to handle instances of non alphanumerica characters
            if not str(s[front_index]).isalnum():
                front_index += 1
                continue

            if not str(s[back_index]).isalnum():
                back_index -= 1
                continue

            # If we have a palindome our index at the front and the back should represent the same character
            # if they don't we return False
            if s[front_index].lower() != s[back_index].lower():
                return False
            front_index += 1
            back_index -= 1

        # If after meeting in the middle we havn't found an error, we can return True
        return True
        

        
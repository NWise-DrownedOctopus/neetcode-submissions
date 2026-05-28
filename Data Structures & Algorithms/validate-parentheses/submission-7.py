class Solution:
    def isValid(self, s: str) -> bool:
        # Ok so if we are using a stack to solve this problem I would assume we can always add a left side chracter to the stack
        # If we encounter a right side chracter we pop the most recent left chracter, and if it matches we good, otherwise fail

        char_stack = []

        left_chars = {'(', '{', '['}

        # We can eliminate any string with an odd length 
        if len(s) % 2 == 1:
            return False

        for char in s:
            if char in left_chars:
                char_stack.append(char)
            else:
                if len(char_stack) == 0:
                    return False
                popped_char = char_stack.pop()
                if popped_char == None:
                    return False
                elif char == ')' and popped_char == '(':
                    continue
                elif char == '}' and popped_char == '{':
                    continue
                elif char == ']' and popped_char == '[':
                    continue
                return False
        
        # If we have any remaining values un accounted for, we return a fail
        if len(char_stack) != 0:
            return False

        return True
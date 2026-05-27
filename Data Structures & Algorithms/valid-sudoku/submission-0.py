class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Ok we need to keep track of a few things to be more efficent
        # If we keep track of the x and y position we could identify which row column and square each element belongs in
        # that way we can check as we go for each structure, rather than having to repeat a loop to check for all three conditions

        # We need to store our entires inside dctionaries that we can quickly check if we have a second entry in
        # We need 9 row dicts, 9 colmn dicts, and 9 bow dicts
        # Each row can have a key that is the x value
        # Each colmn can hava  a key that is the y value
        # Each box number can be found with a helper function
        row_dicts = {}
        column_dicts = {}
        box_dicts = {}

        row = 0
        while row < 9:
            column = 0
            while column < 9: 
                num = board[row][column]
                if num == ".":
                    column += 1
                else:
                    # First check if row already exisit in our first level dictionary
                    # if not we add a row_dict, with a dict entry for the number found
                    if row not in row_dicts:
                        row_dicts[row] = {num: 1} # Create Row Dict with num dict entry inside it
                    else:
                        # If we did find the row dict check if that dict contains the num found
                        if num in row_dicts[row]:
                            return False
                        else:
                            # If not found in dict, we can add a new entry
                            row_dicts[row][num] = 1
                    
                    # Second we do the same for the column
                    if column not in column_dicts:
                        column_dicts[column] = {num: 1} # Create Column Dict with num dict entry inside it
                    else:
                        # If we did find the Column dict check if that dict contains the num found
                        if num in column_dicts[column]:
                            return False
                        else:
                            # If not found in dict, we can add a new entry
                            column_dicts[column][num] = 1

                    # Third we do the same for the box
                    box = self.getBoxNum(int(row), int(column))
                    if box not in box_dicts:
                        box_dicts[box] = {num: 1} # Create box Dict with num dict entry inside it
                    else:
                        # If we did find the box dict check if that dict contains the num found
                        if num in box_dicts[box]:
                            return False
                        else:
                            # If not found in dict, we can add a new entry
                            box_dicts[box][num] = 1                    
                    column += 1
            row += 1        
        return True

    def getBoxNum (self, x: int, y: int) -> int:
        return (x // 3) * 3 + (y // 3)
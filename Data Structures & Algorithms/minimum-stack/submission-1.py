class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.min_stack.append(val)
            return
        else:
            if self.min_stack[-1] < val:
                self.min_stack.append(self.min_stack[-1])
                self.stack.append(val)
            else:
                self.min_stack.append(val)
                self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop(-1)      
        self.min_stack.pop(-1)  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


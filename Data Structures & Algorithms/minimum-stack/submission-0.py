class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_mins) == 0 or self.stack_mins[-1] >= val:
            self.stack_mins.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if len(self.stack_mins) != 0 and self.stack_mins[-1] == popped:
            self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]

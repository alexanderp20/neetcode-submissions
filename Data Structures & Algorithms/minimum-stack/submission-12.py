class MinStack:

    def __init__(self):
        self.myStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)
        self.minStack.append(min(self.minStack[-1] if self.minStack else val, val))

    def pop(self) -> None:
        self.myStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

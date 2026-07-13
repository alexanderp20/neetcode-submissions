class MinStack:

    def __init__(self):
        self.stack = []
        self.valDict = {}
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.valDict[val] = self.valDict.get(val, 0) + 1
        self.minList.append(min(self.minList[-1] if self.minList else val, val))


    def pop(self) -> None:
        self.valDict[self.stack[-1]] -= 1
        self.stack.pop()
        while self.minList and self.valDict[self.minList[-1]] == 0:
            self.minList.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return int(self.minList[-1])

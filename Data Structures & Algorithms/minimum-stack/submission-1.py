class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            s_val = self.stack[-1]
            if val <= s_val[1]:
                self.stack.append((val, val))
            else:
                self.stack.append((val, s_val[1]))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        s_val = self.stack[-1]
        return s_val[1]


    
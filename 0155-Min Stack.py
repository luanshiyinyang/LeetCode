class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            self.s.append((x, x))
        else:
            self.s.append((x, self.getMin()))
        
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1][0]
        

    def getMin(self) -> int:
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
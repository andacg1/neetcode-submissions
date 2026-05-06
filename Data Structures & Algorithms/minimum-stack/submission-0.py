class MinStack:

    def __init__(self):
        self.queue = deque()
        self.minQueue = deque()

    def push(self, val: int) -> None:
        self.queue.append(val)
        if len(self.minQueue) > 0:
            lastMin = self.minQueue[-1]
            self.minQueue.append(min(lastMin, val))
        else:
            self.minQueue.append(val)

    def pop(self) -> None:
        self.queue.pop()
        self.minQueue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.minQueue[-1]
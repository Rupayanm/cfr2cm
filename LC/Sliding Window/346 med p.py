from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.window = deque(maxlen=size)
        self.size = size
        self.windowSum = 0
    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            s=self.window.popleft()
            self.windowSum -= s
        self.window.append(val)
        self.windowSum += val
        return self.windowSum / len(self.window)

a = MovingAverage(3)
print(a.next(1))
print(a.next(10))
print(a.next(3))
print(a.next(5))


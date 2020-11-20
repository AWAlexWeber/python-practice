'''
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

import queue
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.t, self.q, self.s = 0, queue.Queue(), size
        

    def next(self, val: int) -> float:
        # Taking this value, adding it to our moving average
        self.t += val
        self.q.put(val)
        if self.q.qsize() > self.s:
            self.t -= self.q.get()
            
        return self.t / self.q.qsize()
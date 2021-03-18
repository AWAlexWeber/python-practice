''' Given a stream of integers keep track of the running median value. '''

from heapq import heappop, heappush

class StreamOfIntegers:
    def __init__(self):
        self.lowerHeap = list()
        self.upperHeap = list()

    def __balance__(self):
        while len(self.lowerHeap) - 1 > len(self.upperHeap):
            heappush(self.upperHeap, -heappop(self.lowerHeap))
        while len(self.upperHeap) - 1 > len(self.lowerHeap):
            heappush(self.lowerHeap, -heappop(self.upperHeap))

    def push(self, k: int):
        if len(self.upperHeap) > 0 and k >= self.upperHeap[0]:
            heappush(self.upperHeap, k)
        else:
            heappush(self.lowerHeap, -k)

        self.__balance__()

    def getMedian(self) -> int:
        if len(self.lowerHeap) == len(self.upperHeap):
            return (self.lowerHeap[0] + self.upperHeap[0]) / 2
        elif len(self.lowerHeap) > len(self.upperHeap):
            return self.lowerHeap[0]
        else:
            return self.upperHeap[0]

s = StreamOfIntegers()
for i in range(15):
    s.push(i)

print(s.getMedian())
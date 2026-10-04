import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_heap_len = 0
        self.max_heap_len = 0
    

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            self.min_heap_len += 1
        else:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_len += 1
        
        if self.max_heap_len > self.min_heap_len + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            self.max_heap_len -= 1
            self.min_heap_len += 1

        elif self.min_heap_len > self.max_heap_len + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
            self.max_heap_len += 1
            self.min_heap_len -= 1
        

    def findMedian(self) -> float:
        
        if self.max_heap_len > self.min_heap_len:
            return -self.max_heap[0]
        
        if self.min_heap_len > self.max_heap_len:
            return self.min_heap[0]
        
        return (-(self.max_heap[0]) + self.min_heap[0]) / 2


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
                count += 1
        return len(intervals) - count

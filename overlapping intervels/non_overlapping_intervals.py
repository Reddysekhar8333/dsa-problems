# Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

def eraseOverlapIntervals(intervals):
    n = len(intervals)
    if not intervals:
        return 0
    intervals.sort(key = lambda x : x[1]) # sort by end position
    count = 0
    previous_interval = 0
    for i in range(1,n):
        if intervals[i][0] >= intervals[previous_interval][1]:
            previous_interval = i
        else:
            count += 1
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
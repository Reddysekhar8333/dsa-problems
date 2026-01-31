# Given an array of intervals, merge all the overlapping intervals.
# Return an array of non-overlapping intervals.
def merge(intervals):
    intervals.sort(key=lambda x : x[0]) # sort the intervals by start time
    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

intervals = [[1,3],[8,10],[15,18],[2,6]]
print(merge(intervals))
print("-------------------------------")
# check if two intervals overlap
a = [1,5] #interval1
b = [4,6] #interval2
def is_overlap(a, b):
    return  (a[1] > b[0] or a[0] < b[1])
print(is_overlap(a,b))

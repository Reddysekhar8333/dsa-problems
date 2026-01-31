# Given an array of non-overlapping intervals,where intervals[i]=[start,end]
# you need to insert another interval,such that resultant intervals still don't overlap.
# merge intervals if required.

def insert_interval(newInterval,intervals):
    result = []
    i = 0
    n = len(intervals)

    # add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0],intervals[i][0])
        newInterval[1] = max(newInterval[1],intervals[i][1])
        i  += 1
    # add the merged interval
    result.append(newInterval)

    # add remaing intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    # return answer
    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert_interval(newInterval,intervals))
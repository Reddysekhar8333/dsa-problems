# LeetCode 253: Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of conference rooms required.
'''
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
- Meeting [0,30] needs room 1
- Meeting [5,10] needs room 2  
- Meeting [15,20] can use room 2    
'''

import heapq
# Method 1: Min-Heap (Priority Queue)
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    # Min-heap to track ending times
    heap = []
    for start, end in intervals:
        print(f'{start} and {end}')
        # If earliest ending meeting ends before current starts
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # Reuse that room
        # Add current meeting's end time
        heapq.heappush(heap, end)
    return len(heap)
        

intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))
print("------")
print(minMeetingRooms([[7,10],[2,4]]))

# Method 2: Two Pointers (Chronological Sorting)
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    # Separate start and end times
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    
    rooms = 0
    end_ptr = 0
    
    for start in start_times:
        print(start," and ",end_ptr)
        # If a meeting ended before current starts
        if start >= end_times[end_ptr]:
            end_ptr += 1  # Reuse that room
        else:
            rooms += 1  # Need new room
    return rooms

print("-------------two pointers approach--------------")
intervals = [[0,10], [5,15], [10,20]]
print(minMeetingRooms(intervals))
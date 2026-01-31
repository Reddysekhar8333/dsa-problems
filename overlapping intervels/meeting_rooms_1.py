# LeetCode 252: Meeting Rooms I
# Given an array of meeting time intervals intervals where 
# intervals[i] = [start_i, end_i], determine if a person could attend all meetings.
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

def meetingRooms(intervals):
    intervals.sort(key = lambda x : x[0])
    prev = 0
    for i in range(1,len(intervals)):
        if intervals[prev][1] <= intervals[i][0]:
            prev = i
        else:
            return False
    return True

intervals = [[0,30],[5,10],[15,20]]
print(meetingRooms(intervals))

                   
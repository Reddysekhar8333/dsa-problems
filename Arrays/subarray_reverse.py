# Q : Given an array of n distinct(unique) integers, The task is to check whether reversing one subarray can make the array sorted or not.
#  if the array is already sorted or can be made sorted by reversing one subarray, print "YES" otherwise print "NO" .

def sub_array_reverse(arr):
    start= -1
    end= -1
    temp=sorted(arr)
    for i in range(len(arr)):
        if arr[i]!=temp[i]:
            start=i
            break
    for i in range(len(arr)-1,0,-1):
        if arr[i]!=temp[i]:
            end=i
            break
    for i in range(start,end):
        if arr[i]<arr[i+1]:
            return "NO"
    return "YES"
n=[1,2,5,4,3,6,7,10,8]
print(sub_array_reverse(n))
n1=[1,2,3,4,5,6]
print(sub_array_reverse(n1))
n2=[1,2,5,4,3,6,7]
print(sub_array_reverse(n2))
    
    
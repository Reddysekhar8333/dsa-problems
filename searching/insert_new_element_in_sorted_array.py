'''find the index where we can insert a new element'''
# the new element is not there in the array

def funtion(arr,ele):
    low=0
    high=len(arr)
    while low<high:
        mid = (high+low)//2
        if arr[mid] < ele:
            low = mid+1
        else:
            high=mid
    # Step 2: Insert at the found position
    arr.insert(low, ele)
    return arr

arr=[1,2,3,4,5,7,8,9,10]
print(funtion(arr,33))


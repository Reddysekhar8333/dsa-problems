def find_element_infinite_sorted_array(arr,target):
    low=0
    high=1
    while arr[high]<target:
        low=high+1
        high*=2
    return binary_search(arr,target,low,high)
def binary_search(arr,target,low,high):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

if __name__=="__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 35, 40, 45]  # Assume it's infinite
    ans=find_element_infinite_sorted_array(arr,21)
    print(ans)
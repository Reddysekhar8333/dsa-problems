#Find a ceil of a sorted Array
#Find a floor of a sorted Array
arr=[19,23,56,61,72,88,92]
def brute_force(arr:list,ele):# O(n) time complexity
    n=len(arr)
    ceil_ele=None
    floor_ele=None
    if ele in arr:
        ceil_ele = ele
        floor_ele=ele
        return ceil_ele,floor_ele
    if ele < arr[0]:
        return arr[0],None
    if ele > arr[n-1]:
        return None,arr[0]
    pointer1=0
    pointer2=1
    while pointer2 < n:
        if arr[pointer1]<ele and arr[pointer2]>ele:
            ceil_ele=arr[pointer2]
            floor_ele=arr[pointer1]
            return ceil_ele,floor_ele
        else:
            pointer1+=1
            pointer2+=1 
def optimal(arr,ele):# O(log n) time complexity
    "using binary search"
    n=len(arr)
    low,high=0,n-1
    floor_ele,ceil_ele=None,None
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==ele:
            return arr[mid],arr[mid]
        if arr[mid]<ele:
            floor_ele=arr[mid]
            low=mid+1
        else:
            ceil_ele=arr[mid]
            high=mid-1
    return ceil_ele,floor_ele

if __name__=="__main__":
    print("--------brute force-------")  
    print("(ceil , floor)")
    print(brute_force(arr,13))
    print("---------using binary search----------")
    print(optimal(arr,45))



'''NOTE: span of array =max element - min element'''
# span = max-min
arr=[20,42,88,10,99,6,33,7]

def span_of_array(arr:list):
    if not arr:
        return None
    min_ele=arr[0]
    max_ele=arr[0]
    for i in arr[1:]: # arr is also works but, arr[0] is already assigned to min_ele & max_ele 
        if i>max_ele:
            max_ele=i
        if i<min_ele:
            min_ele=i
    return max_ele-min_ele

print(span_of_array([]))
print(span_of_array(arr))

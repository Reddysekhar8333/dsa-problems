#using recursion write the three funtion to reverse string ,number,array
string="reddy"
number=12345
arr=[1,2,3,4,5]
def reverse_str(arr,s="",n=len(arr)-1):
    "reverse the string"
    if n==-1:
        return s
    return reverse_str(arr,s+arr[n],n-1)
def reverse_num(num,rev=0):
    if num==0:
        return rev
    return reverse_num( num//10, (rev*10)+(num%10) ) 

def reverse_arr(arr,left=0,right=None):
    if right is None:
        right=len(arr)-1
    if left>=right:
        return arr
    arr[left],arr[right]=arr[right],arr[left]
    return reverse_arr(arr,left+1,right-1)
    

print(reverse_str(string))
print(reverse_num(number))
print(reverse_arr(arr))
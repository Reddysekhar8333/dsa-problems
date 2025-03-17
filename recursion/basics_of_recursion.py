#sum of the digits
def sum_of_digits(n):
    if n==0:
        return 0
    return (n%10)+sum_of_digits(n//10)

#product of the digits
def product_of_digits(n):
    if n<=9:
        return n
    return (n%10)*product_of_digits(n//10)

#print n numbers reversely
def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)

#print n numbers orderly using recursion
def funr(n):
    if n==0:
        return
    funr(n-1)
    print(n,end=" ")
# reverse a number, ex:1234 ==>4321
'''there are few ways to solve using recursion'''
def reverse1(n,rev=0):
    """using integer division & modulus"""
    if n==0:
        return rev
    return reverse1(n//10, rev*10 + n % 10)
def reverse2(n):
    """using string conversion & recursion"""
    n=str(n)
    if len(n)==1:
        return n
    return n[-1]+reverse2(n[:-1])
# check if the number is palindrome
def is_palindrome(n):
    n=str(n)
    def check(string,left,right):
        if left>=right:
            return True
        if string[left]!=string[right]:
            return False
        return check(string,left+1,right-1)
    return check(n,0,len(n)-1)
#count no. of zeros in a number
'''ex:30204 ==> 2 '''
def count_zeros(n):
    def helper(n,count):
        if n==0:
            return count
        remainder=n%10
        if remainder==0:
            return helper(n//10,count+1)
        return helper(n//10,count)
    return helper(n,0)

#SUM OF ELEMENTS IN AN ARRAY
def sum_of_arr(arr,result=0,n=None):
    if n is None:
        n=len(arr)-1
    if n==-1:
        return f"sum of array :{result}"
    return sum_of_arr(arr,result+arr[n],n-1)
    

if __name__=="__main__":
    print(sum_of_digits(12345))
    print(product_of_digits(12345))
    print(fun(5))
    print(funr(5))
    print("reverse1:")
    print(reverse1(12345))
    print("reverse2:")
    print(reverse2(67890))
    print("palindrome:")
    print(is_palindrome(12321))
    print("count zeros :")
    print(count_zeros(30204))
    print(sum_of_arr([1,2,3,4,5]))
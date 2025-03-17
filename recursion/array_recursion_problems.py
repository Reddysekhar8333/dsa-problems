class arrays_recursion:
    def is_sort(self,arr,index)->bool:
        "find if array is sorted or not"
        #T.C=O(n) S.C=O(n)        
        if index == len(arr)-1:#base condition
            return True
        return arr[index]<=arr[index+1] and self.is_sort(arr,index+1)
    
    def linear_search(self,arr, target, index=0):
        "linear search using recursion"
        # Base case: If index reaches the end, return -1 (not found)
        if index == len(arr):
            return -1
        # If the current element matches the target, return index
        if arr[index] == target:
            return f"element found at {index}"
        # Recursive call for the next index
        return self.linear_search(arr, target, index + 1)
    def find_index_target(self,arr,target,res=[],index=0):
        n=len(arr)
        #base condition
        if index == n:
            return res
        if arr[index] == target:
            res.append(index+1)
        return self.find_index_target(arr,target,res,index+1)
    def find_index_target2(self,arr,target,index=0):
        n=len(arr)
        res=[]
        if index == n:
            return res
        if arr[index] == target:
            res.append(index+1)
        answercalls=self.find_index_target2(arr,target,index+1)
        res.extend(answercalls)
        return res
    def rotated_binary_search():
        pass
            

obj=arrays_recursion()
print(obj.is_sort([1,2,3,3,5,6,7],0))
print(obj.linear_search([1,2,3,4,5,6,7],9))
print(obj.find_index_target([2,2,5,4,6,4,6,4,2],2))
print(obj.find_index_target2([2,2,5,4,6,4,6,4,2],2))
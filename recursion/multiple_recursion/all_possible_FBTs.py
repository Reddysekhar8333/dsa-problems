# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int): 
        # Full binary tree must have odd number of nodes
        if n % 2 == 0:
            return []
        
        # Base case: single node
        if n == 1:
            node = TreeNode(0)
            return [node]
        
        all_trees = []
        
        # Try all odd distributions
        # left_count: 1, 3, 5, ..., n-2
        for left_count in range(1, n, 2):
            right_count = n - 1 - left_count
            
            # Generate all possible left subtrees
            left_trees = self.allPossibleFBT(left_count)
            
            # Generate all possible right subtrees
            right_trees = self.allPossibleFBT(right_count)
            
            # Combine each left with each right
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        
        return all_trees
    
obj = Solution()

print(obj.allPossibleFBT(5))

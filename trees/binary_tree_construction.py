
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def inorder_traversal(root):
    if not root:
        return 
    inorder_traversal(root.left)
    print(root.val,end="-")
    inorder_traversal(root.right)
def preorder_traversal(root):
    if not root:
        return
    print(root.val,end="-") 
    preorder_traversal(root.left)
    preorder_traversal(root.right)
def postorder_traversal(root):
    if not root:
        return 
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val,end="-")

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
print('pre-order')
preorder_traversal(root)
print('\nin-order')
inorder_traversal(root)
print('\npost-order')
postorder_traversal(root)
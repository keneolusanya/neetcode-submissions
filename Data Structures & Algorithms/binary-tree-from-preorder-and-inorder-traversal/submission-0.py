# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        if len(preorder) == 0:
            return
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        
        rootVal = preorder[0]
        rootIndex = 0

        while inorder[rootIndex] != rootVal:
            rootIndex += 1
        
        preorder.pop(0)
       
        leftInOrder = inorder[:rootIndex]
        rightInOrder = inorder[rootIndex + 1:]
        len1 = len(leftInOrder)
        leftPreOrder = preorder[:len1]
        rightPreOrder = preorder[len1:]

        rootLeft = self.buildTree(leftPreOrder, leftInOrder)
        rootRight = self.buildTree(rightPreOrder, rightInOrder)
        
        root.left = rootLeft
        root.right = rootRight

        return root

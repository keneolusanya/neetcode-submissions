# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (not root): 
            return 0

        elif (not(root.left) and not(root.right)):
            return 1

        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

            if leftDepth > rightDepth:
                return 1 + leftDepth
            else:
                return 1 + rightDepth
        






# ###########
# if (root == nullptr) {
#             return 0;
#         }

#         else if ((root->left == nullptr) && root->right == nullptr) {
#             return 1;
#         }

#         else {
#             int leftDepth = maxDepth(root->left);
#             int rightDepth = maxDepth(root->right);
#             // max function in c++?

#             if (leftDepth > rightDepth) {
#                 return 1 + leftDepth;
#             }

#             else {
#                 return 1 + rightDepth;
#             }
#         }
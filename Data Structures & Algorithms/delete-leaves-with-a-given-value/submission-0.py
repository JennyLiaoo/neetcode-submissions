# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        input: node (root), int (target)
        output: tree with deleted val as leaves

        Q: more than one leaf node with val target?
        Q: if we delete a leaf node, and it creates another with that val do we delete that too.
        - dfs(node) -> is_deleted bool after later deletions. 
        - if left is deleted/None and right is deleted/None, we need to decide whether current node needs to be deleted. if so, then propogate this information up to parent node
        '''

        def dfs(node):
            if node is None:
                return True
            if node.left is None and node.right is None and node.val == target:
                return True
            if node.left is None and node.right is None:
                return False
            remove_left = dfs(node.left)
            remove_right = dfs(node.right)
            if remove_left:
                node.left = None
            if remove_right:
                node.right = None
            if remove_left and remove_right and node.val == target:
                return True

            return False
        dfs(root)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root

        
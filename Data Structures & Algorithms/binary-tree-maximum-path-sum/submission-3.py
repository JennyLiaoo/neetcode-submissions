# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        input: root of BT
        output: max path sum of any path

        - path can be in left, right, or across the root
        Q: can have negative nodes? Yes
        At each node store: max sum including that node
        at end take a max over stored nodes
        max_path_through[node] = maximum sum of path that includes node
        max_path_through[node] = max(node.val, node.val+left_sum, node.val+right_sum, node.val+left_sum+right_sum)
        '''
        max_path_sum = float("-inf")
        def dfs(node):  # sets the max path sum through a node but returns the max path sum inclusive of the node and downwards (not across) cuz this is the value u need when defining ur max path sum through the parent node         
            nonlocal max_path_sum
    
            max_path_sum_current = node.val
            max_down = 0
            left = 0
            right = 0
            if node.left is not None:
                left = dfs(node.left)
                max_path_sum_current = max(max_path_sum_current, node.val+left)
                max_down = max(max_down, left)

            if node.right is not None:
                right = dfs(node.right)
                max_path_sum_current = max(max_path_sum_current, node.val+right)
                max_down = max(max_down, right)
            
            if node.left is not None and node.right is not None:
                max_path_sum_current = max(max_path_sum_current, node.val+right+left)

            max_path_sum = max(max_path_sum, max_path_sum_current)
            return node.val + max_down
        dfs(root)
        return max_path_sum   
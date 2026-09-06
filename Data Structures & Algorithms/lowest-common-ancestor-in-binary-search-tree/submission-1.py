# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        input: BST, p, q
        output: LCA

        Q: return node or val?
        Q: unique or not
        Q: LCA => node such that both p and q are descendants
        Q: is it possible for no ancestor? i.e one node is ancestor of another
        Q: p and q guaranteed in tree?
        Q: Connected with <=2 children

        if not one anc of other
        LCA => val s.t p is on left and q is on right
        i.e at node, check if one node in left while other in right. if so, then LCA
        if both in same side, this is not LCA as they are on the same side, thus there must be some other ndoee as LCA

        if node == p or q: when we encounter that one first, that is LCA
        '''
        curr_node = root
        while curr_node != None:
            if curr_node.val == p.val:
                return p
            elif curr_node.val == q.val:
                return q
            elif p.val < curr_node.val and q.val>curr_node.val or q.val < curr_node.val and p.val>curr_node.val:
                return curr_node
            else:   # in same side
                if p.val < curr_node.val:
                    # both in left
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
                



        
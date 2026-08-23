# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # a string with # separating stuff
    # i is node, 2*i and 2*i+1
    # or like save it in pre/post/in order
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        # preorder?
        def dfs(node):
            if node == None:
                s.append("N#")
            else:
                s.append(str(node.val) + "#")
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ''.join(s)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        strings = data.split('#')
        i = 0
        def dfs():  # returns the tree built yk?
            nonlocal i
            value = strings[i]
            i += 1
            if value == 'N':
                return None
            else:
                new_node = TreeNode(int(value))
                new_node.left = dfs()
                new_node.right = dfs()
                return new_node
            

        tree = dfs()
        return tree




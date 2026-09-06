class Node:
    def __init__(self,val):
        self.val = val
        self.children = dict()  # c -> Node
        self.is_end = False

class WordDictionary:
    '''
    at most two dots => O(n) * 26 * 26 = O(n)
    '''

    def __init__(self):
        self.trie = Node(None)
  

    def addWord(self, word: str) -> None:
        i = 0
        curr_node = self.trie
        while i < len(word):
            if word[i] not in curr_node.children:
                curr_node.children[word[i]] = Node(word[i])
        
            curr_node = curr_node.children[word[i]]
            if i == len(word) - 1:
                curr_node.is_end = True
            i+=1
        
    def search(self, word: str) -> bool:
        curr_node = self.trie
        def dfs(node, i):
            if i == len(word) and node.is_end:
                return True
            elif i == len(word): return False
            current_char = word[i]
            if current_char in node.children:
                return dfs(node.children[current_char], i+1)
            elif current_char == '.':
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c in node.children and dfs(node.children[c], i+1):
                        return True
                return False
            else:
                return False

        return dfs(self.trie, 0)
        

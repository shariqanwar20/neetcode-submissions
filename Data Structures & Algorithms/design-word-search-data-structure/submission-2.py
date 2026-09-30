class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = ord(c) - ord('a')

            if curr.children[i] == None:
                curr.children[i] = TreeNode()
            curr = curr.children[i]

        curr.end = True

    def search(self, word: str) -> bool:
        

        def dfs(char_index, node):
            curr = node

            for c in range(char_index, len(word)):
                if word[c] == ".":
                    for child in curr.children:
                        if child == None:
                            continue
                        if dfs(c + 1, child):
                            return True
                    return False
                        
                else:
                    i = ord(word[c]) - ord('a')
                    if curr.children[i] == None:
                        return False
                    curr = curr.children[i]
            return curr.end
        return dfs(0, self.root)
                    
                
            
        

        


            


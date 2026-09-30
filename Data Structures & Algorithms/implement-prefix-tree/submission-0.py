class PrefixTreeNode:
    def __init__(self, val, end = False):
        self.val = val
        self.children = [None for _ in range(26)]
        self.end = end
        
class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word) - 1):
            char_val = ord(word[i]) - ord('a')
            if not curr.children[char_val]:
                curr.children[char_val] = PrefixTreeNode(word[i])
            curr = curr.children[char_val]

        char_val = ord(word[len(word) - 1]) - ord('a')
        if not curr.children[char_val]:
            curr.children[char_val] = PrefixTreeNode(word[len(word) - 1])
        curr.children[char_val].end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word) - 1):
            char_val = ord(word[i]) - ord('a')
            if not curr.children[char_val]: return False
            curr = curr.children[char_val]
        char_val = ord(word[len(word) - 1]) - ord('a')

        if not curr.children[char_val] or not curr.children[char_val].end:
            return False
        return True 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            char_val = ord(prefix[i]) - ord('a')
            if not curr.children[char_val]: return False
            curr = curr.children[char_val]
        return True 
        
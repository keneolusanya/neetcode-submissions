class LetterNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = LetterNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children.keys():
                curr.children[c] = LetterNode()
            curr = curr.children[c]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if c not in curr.children.keys():
                        return False
                    curr = curr.children[word[i]]
                
            return curr.isEndOfWord

        return dfs(0, self.root)
        

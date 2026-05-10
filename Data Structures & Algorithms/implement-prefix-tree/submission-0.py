class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr.keys():
                curr[char] = {}
            curr = curr[char]
        curr["end"] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr.keys():
                return False
            curr = curr[char]
        return curr.get("end", False) == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr.keys():
                return False
            curr = curr[char]
        return True
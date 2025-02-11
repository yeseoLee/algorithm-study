# 66ms / 32.21MB
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for idx in range(len(word)):
            if word[idx] not in node.children.keys():
                node.children[word[idx]] = TrieNode()
            node = node.children[word[idx]]
            if idx == len(word) - 1:
                node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for idx in range(len(word)):
            if word[idx] not in node.children.keys():
                return False
            node = node.children[word[idx]]
            if idx == len(word) - 1 and node.word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for idx in range(len(prefix)):
            if prefix[idx] not in node.children.keys():
                return False
            node = node.children[prefix[idx]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 트라이(Trie)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# 예시
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # 출력: True
print(trie.search("banana"))  # 출력: True
print(trie.search("orange"))  # 출력: True
print(trie.search("grape"))  # 출력: False

print(trie.starts_with("app"))  # 출력: True
print(trie.starts_with("ban"))  # 출력: True
print(trie.starts_with("gr"))  # 출력: False

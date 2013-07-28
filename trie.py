class TrieNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = {}

    def __str__(self):
        return '<%s:%s %s>' % (self.key, self.value,
                               ','.join(str(c)
                                        for c in self.children.values()))

    def leaves(self):
        leaves = []
        if not self.children:
            leaves.append(self.key)
        for child in self.children.values():
            leaves.extend(child.leaves())
        return leaves


class Trie:
    '''A prefix tree.'''
    def __init__(self):
        self.root = TrieNode('', None)

    def put(self, key, value):
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch, None)
            node = node.children[ch]
        node.key = key
        node.value = value

    def get(self, key):
        node = self.root
        for ch in key:
            if ch not in node.children:
                return None
            else:
                node = node.children[ch]
        return node.value

    def matches(self, key):
        node = self.root
        for ch in key:
            if ch not in node.children:
                return []
            else:
                node = node.children[ch]
        return sorted(node.leaves(), key=len)

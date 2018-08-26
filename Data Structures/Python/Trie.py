from collections import deque
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node(node.val+c)
                node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.isWord        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True 
    
    def __str__(self):
        """
        Uses breadth first search to print out all elems and child nodes of Trie
        :rtype: string
        """
        s = ''
        que = deque()
        que.append(self.root)
        while que:
            node = que.popleft()
            for key in node.children:
                que.append(node.children[key])
            s += node.val
            print(s)
        return s
        

    
class Node(object):
    def __init__(self, _val):
        """
        Initialize your data structure here.
        """
        self.val = _val
        self.children = {}
        self.isWord = False

tr = Trie()
tr.insert('hello')
print(tr.startsWith('e'))



        
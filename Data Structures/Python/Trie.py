
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
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
    
    def __str__(self):
        """
        Uses breadth first search to print out all elems and child nodes of Trie
        :rtype: string
        """
        s = ''
        

    
class Node(object):
    def __init__(self, _val):
        """
        Initialize your data structure here.
        """
        self.val = _val
        self.children = {}

tr = Trie()
tr.insert('hello')



        
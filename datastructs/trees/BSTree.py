class BSTreeNode(object):
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None

class BSTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        newNode = BSTreeNode()
        newNode.key = key
        newNode.value = value

        if not self.root:
            self.root = newNode
            return

        cur = self.root

        while cur:
            if key < cur.key:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left = newNode
                    return  
            elif key > node.key:
                if node.right:
                    cur = cur.right
                    continue
                else:
                    cur.right = newNode
                    return 
            else:
                node.value = value
                return node
            

    def get(self, key):
        node, parent = self._getNodeAndParentForKey(key)
        return node.value if node else None

    def remove(self, key):
        if self.root.key == key and self.root.left is None and self.root.right is None:
            self.root = None

        parent = None
        cur = root
        while cur:
            if key < cur.key:
                parent = cur
                cur = cur.left
            elif key > cur.key:
                parent = cur
                cur = cur.right
            else:
                
    def _getNodeAndParentForKey(self, key):
        cur = self.root
        parent = None

        while cur:
            if key < cur.key:
                parent = cur
                cur = cur.left
            elif key > node.key:
                parent = cur
                cur = cur.right
            else:
                return cur, parent

        return (None, parent)   



def findMin(node):
    cur = node
    while cur.left:
        cur = cur.left
    return cur

        
    

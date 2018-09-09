def TTreeNode(object):
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.values = []

        
def TTree(object):
    def __init__(self, arraysize=5):
        self.root = None

    def search(self, value):
        if not self.root:
            return None


        if value in self.root:
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass



import GraphStoreIface

class Database(GraphStoreIface.GraphStoreIface):
    def __init__(self):
        self._path = None
    def connect(self,path):
#        if not os.path.exists(os.path.join(path, ".meta","version")):
#            raise Exception("Not a database dir")
#        if not os.path.exists(os.path.join(path, ".meta","format")):
#            raise Exception("Not a database dir")

#        self._path = path
#
#        f = file(os.path.join(self._path,".meta","version"), "r")
#        self._db_version = int(f.readline())
#        f.close()
#
#        if not self._db_version in SUPPORTED_VERSIONS:
#            raise Exception("Unsupported version "+str(self._db_version))
        
    def createGraph(self, namespace='/', directed=True):   raise NotImplementedError
    def allGraphs(self, namespace):   raise NotImplementedError

    def setDbMetainfo(self, key, value):   raise NotImplementedError
    def dbMetainfo(self,key):   raise NotImplementedError


    def addVertex(self, graph):   raise NotImplementedError
    def deleteVertex(graph, vertex_id):   raise NotImplementedError


    def addNEdge(self, graph, vertices):   raise NotImplementedError
    def deleteNEdge(self, graph, vertex_tuple):   raise NotImplementedError

   
    def createInfoset(self, graph, infoset_type, name=None):   raise NotImplementedError
    def deleteInfoset(self, graph, infoset_id, namespace=None):   raise NotImplementedError
    def getInfosetType(self, graph, infoset_id, namespace=None):   raise NotImplementedError


    def setInfosetValue(self, graph, entity, infoset_id_or_tuple, value_or_tuple):   raise NotImplementedError
    def getInfosetValue(self, graph, entity, infoset_id_or_tuple):   raise NotImplementedError




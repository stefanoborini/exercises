class GraphStoreIface:
    def __init__(self):   raise NotImplementedError
    def connect(self,path):   raise NotImplementedError
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




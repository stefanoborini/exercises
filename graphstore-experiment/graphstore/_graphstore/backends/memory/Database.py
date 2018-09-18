import Graph
import Infoset
from ... import GraphStoreIface
from ... import InfosetType

import types

class Database(GraphStoreIface.GraphStoreIface):
    def __init__(self): # fold>>
        self._path = None
        self._graphlist = {}
        self._ns_graphlist = {}
        self._db_metainfo = {}
        # <<fold
    def connect(self,path): # fold>>
        self._path = path
        pass 
        # <<fold

    def setDbMetainfo(self, key, value): # fold>>
        self._db_metainfo[key]=value
        # <<fold
    def dbMetainfo(self,key): # fold>>
        return self._db_metainfo[key]
        # <<fold

    def createGraph(self, namespace='/', name=None, directed=True): # fold>>
        g = Graph.Graph(name)
        if not self._ns_graphlist.has_key(namespace):
            self._ns_graphlist[namespace] = {}
        self._graphlist[g.uuid()] = g
        self._ns_graphlist[namespace][g.uuid()] = g
        return g.uuid()
            # <<fold 
    def graphNamespace(self, graph_id): # fold>>
        g = self._graphlist[graph_id]
        for namespace, graphs_dict in self._ns_graphlist.items():
            if g in graphs_dict.values():
                return namespace

        return None
        # <<fold
    def graphName(self, graph_id): # fold>>
        g = self._graphlist[graph_id]
        return g.name()
        # <<fold
    def allGraphs(self, namespace=None): # fold>>
        return self._graphlist.keys()
        # <<fold

    def createVertex(self, graph_id): # fold>>
        g = self._graphlist[graph_id]
        return g.createEntity()
        # <<fold
    def deleteVertex(self, graph_id, vertex_id): # fold>>
        g = self._graphlist[graph_id]
        return g.deleteEntity(vertex_id)
            # <<fold 
    def vertexCount(self,graph_id): # fold>>
        g = self._graphlist[graph_id]
        return len(g.entityList(1))
        # <<fold

    def createNEdge(self, graph_id, vertices): # fold>>
        g = self._graphlist[graph_id]
        return g.createEntity(vertices)
        # <<fold
    def deleteNEdge(self, graph_id, vertex_tuple): # fold>>
        g = self._graphlist[graph_id]
        return g.deleteEntity(vertex_tuple)
        # <<fold
    def nEdgeCount(self, graph_id, dimensionality): # fold>>
        g = self._graphlist[graph_id]
        return len(g.entityList(dimensionality))
        # <<fold 

    def createInfoset(self, graph_id, infoset_type, name=None): # fold>>
        g = self._graphlist[graph_id]
        i = Infoset.Infoset(g, infoset_type, name=name)
        return i.uuid()
        # <<fold
    def deleteInfoset(self, graph_id, infoset_id): # fold>>
        g = self._graphlist[graph_id]
        l = g.getInfosets(uuid=infoset_id)
        if len(l) != 1:
            raise Exception()
        else:
            g.deleteInfoset(l[0])
            # <<fold 
    def infosetType(self, graph_id, infoset_id): # fold>>
        g = self._graphlist[graph_id]
        l = g.getInfosets(uuid=infoset_id)
        if len(l) != 1:
            raise Exception()
        else:
            return l[0].type()
        # <<fold
    def allInfosets(self, graph_id, dimensionality=None): # fold>>
        g = self._graphlist[graph_id]
        infosets = g.getInfosets(dimensionality=dimensionality)
        return [l.uuid() for l in infosets]
        # <<fold
        
    def setInfosetValue(self, graph_id, infoset_id_list, entity_id, value_list): # fold>>
        g = self._graphlist[graph_id]
        if len(value_list) != len(infoset_id_list):
            raise ValueError("len of infoset_id list != len of value list")

        infosets = map(lambda x: g.getInfosets(uuid=x)[0], infoset_id_list)
        for i, v in zip(infosets, value_list):
            i.setValue(entity_id, v)

            # <<fold 
    def infosetValue(self, graph_id, infoset_id_list, entity_id): # fold>>
        g = self._graphlist[graph_id]

        infosets = map(lambda x: g.getInfosets(uuid=x)[0], infoset_id_list)
        return tuple([x.value(entity_id) for x in infosets])
        
        # <<fold 

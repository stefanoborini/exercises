# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../../../"));
import unittest
import time


from graphstore._graphstore.backends.memory import Database
from graphstore._graphstore import InfosetType

def moduleDir():
    return os.path.dirname(__file__)

class TestDatabase(unittest.TestCase):
    def testInitX(self): # fold>>
        g = Database.Database()

        self.assertEqual(g.__class__, Database.Database)
    # <<fold
    def testConnect(self): # fold>>
        g = Database.Database()
        g.connect("db_testConnect")
        
        self.assertEqual(0,0)
    # <<fold

    def testDbMetainfo(self): # fold>>
        g = Database.Database()
        g.connect("db_testDbMetainfo")

        g.setDbMetainfo("test","123")
        self.assertEqual(g.dbMetainfo("test"), "123")
        self.assertRaises(KeyError, g.dbMetainfo, "nothing")
    # <<fold

    def testCreateGraph(self): # fold>>
        g = Database.Database()
        g.connect("db_testCreateGraph")
        
        id = g.createGraph()

        self.assertNotEqual(id, None)
        # <<fold 
    def testCreateGraphNamespace(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateGraphNamespace")
        
        id = db.createGraph(namespace='/foo', name="grafo")
        self.assertEqual(db.graphNamespace(id), "/foo")
        self.assertEqual(db.graphName(id), "grafo")
        # <<fold 
    def testAllGraphs(self): # fold>>
        g = Database.Database()
        g.connect("db_testAllGraphs")
        
        id1 = g.createGraph()
        id2 = g.createGraph()

        self.assertEqual(len(g.allGraphs()),2)
        self.assertTrue(id1 in g.allGraphs())
        self.assertTrue(id2 in g.allGraphs())
        # <<fold 

    def testCreateVertex(self): # fold>>
        g = Database.Database()
        g.connect("db_testCreateVertex")

        graph = g.createGraph()
        v1 = g.createVertex(graph)
        v2 = g.createVertex(graph)

        self.assertNotEqual(v1, None)
        self.assertNotEqual(v2, None)
        self.assertNotEqual(v1, v2)
    # <<fold 
    def testDeleteVertex(self): # fold>>
        g = Database.Database()
        g.connect("db_testDeleteVertex")

        graph = g.createGraph()
        v1 = g.createVertex(graph)
        v2 = g.createVertex(graph)

        self.assertEqual(g.vertexCount(graph),2)
        g.deleteVertex(graph, v1)
        self.assertEqual(g.vertexCount(graph),1)
        g.deleteVertex(graph, v2)
        self.assertEqual(g.vertexCount(graph),0)
    # <<fold
    def testVertexCount(self): # fold>>
        g = Database.Database()
        g.connect("db_testVertexCount")

        graph = g.createGraph()
        v1 = g.createVertex(graph)
        v2 = g.createVertex(graph)

        self.assertEqual(g.vertexCount(graph),2)
    # <<fold 

    def testCreateNEdge(self): # fold>>
        db = Database.Database()
        db.connect("db_testAddNEdge")

        graph = db.createGraph()
        v1 = db.createVertex(graph)
        v2 = db.createVertex(graph)
        v3 = db.createVertex(graph)
        v4 = db.createVertex(graph)
        e1 = db.createNEdge(graph, (v1,v2))
        e2 = db.createNEdge(graph, (v2,v3))
        e3 = db.createNEdge(graph, (v3,v4))
        e4 = db.createNEdge(graph, (v1,v2,v3))
        e5 = db.createNEdge(graph, (v1,v2,v3,v4))
        self.assertNotEqual(v1, None)
        self.assertNotEqual(v2, None)
        self.assertNotEqual(v3, None)
        self.assertNotEqual(v4, None)
        self.assertNotEqual(e1, None)
        self.assertNotEqual(e2, None)
        self.assertNotEqual(e3, None)
        self.assertNotEqual(e4, None)
        self.assertNotEqual(e5, None)
        
    # <<fold
    def testDeleteNEdge(self): # fold>>
        g = Database.Database()
        g.connect("db_testDeleteNEdge")

        graph = g.createGraph()
        v1 = g.createVertex(graph)
        v2 = g.createVertex(graph)
        v3 = g.createVertex(graph)
        v4 = g.createVertex(graph)
        e1 = g.createNEdge(graph, (v1,v2))
        e1 = g.createNEdge(graph, (v2,v3))
        e1 = g.createNEdge(graph, (v3,v4))
        
        self.assertEqual(g.nEdgeCount(graph,2),3)
        g.deleteNEdge(graph, (v2,v3))
        self.assertEqual(g.nEdgeCount(graph,2),2)
    # <<fold
    def testNEdgeCount(self): # fold>>
        db = Database.Database()
        db.connect("db_testAddNEdge")

        graph = db.createGraph()
        v1 = db.createVertex(graph)
        v2 = db.createVertex(graph)
        v3 = db.createVertex(graph)
        v4 = db.createVertex(graph)
        e1 = db.createNEdge(graph, (v1,v2))
        e2 = db.createNEdge(graph, (v2,v3))
        e3 = db.createNEdge(graph, (v3,v4))
        e4 = db.createNEdge(graph, (v1,v2,v3))
        e5 = db.createNEdge(graph, (v1,v2,v3,v4))
        
        self.assertEqual(db.vertexCount(graph),4)
        self.assertEqual(db.nEdgeCount(graph,2),3)
        self.assertEqual(db.nEdgeCount(graph,3),1)
        self.assertEqual(db.nEdgeCount(graph,4),1)
        self.assertEqual(db.nEdgeCount(graph,5),0)
    # <<fold

    def testCreateInfoset(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph = db.createGraph()
        self.assertEqual(len(db.allInfosets(graph)),0)

        id1 = db.createInfoset(graph, InfosetType.InfosetType("http://foo",0))
        id2 = db.createInfoset(graph, InfosetType.InfosetType("http://bar",1))

        self.assertNotEqual(id1, None)
        self.assertNotEqual(id2, None)

        self.assertEqual(len(db.allInfosets(graph)),2)
    # <<fold
    def testDeleteInfoset(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph = db.createGraph()
        id = db.createInfoset(graph, InfosetType.InfosetType("http://foo",0))
        self.assertEqual(len(db.allInfosets(graph)),1)
        
        db.deleteInfoset(graph, id)
        self.assertEqual(len(db.allInfosets(graph)),0)
    # <<fold
    def testGetInfosetType(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph = db.createGraph()
        id = db.createInfoset(graph, InfosetType.InfosetType("http://foo",3))
        
        type = db.infosetType(graph, id)
        self.assertEqual(type.typeURI(), "http://foo")
        self.assertEqual(type.dimensionality(), 3)
        # <<fold 
    def testAllInfosets(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph = db.createGraph()
        self.assertEqual(len(db.allInfosets(graph)),0)

        id1 = db.createInfoset(graph, InfosetType.InfosetType("http://foo",0))
        self.assertEqual(len(db.allInfosets(graph)),1)
        id2 = db.createInfoset(graph, InfosetType.InfosetType("http://bar",1))
        self.assertEqual(len(db.allInfosets(graph)),2)
        self.assertEqual(len(db.allInfosets(graph, dimensionality=0)),1)
        self.assertEqual(len(db.allInfosets(graph, dimensionality=1)),1)
        self.assertEqual(len(db.allInfosets(graph, dimensionality=2)),0)
    # <<fold
        
    def testSetGetInfosetValue(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph_id = db.createGraph()
        graph_type = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#GraphType",0))
        name = db.createInfoset(graph_id, InfosetType.InfosetType("http://example/com/#Name",1))
        relationship = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#Relationship",2))

        v1 = db.createVertex(graph_id)
        v2 = db.createVertex(graph_id)
        e1 = db.createNEdge(graph_id, (v1,v2))
   
        db.setInfosetValue(graph_id, (graph_type,), None, ("Friendship",))
        db.setInfosetValue(graph_id, (name,), v1, ("Alice",))
        db.setInfosetValue(graph_id, (name,), v2, ("Bob",))
        db.setInfosetValue(graph_id, (relationship,), e1, ("knows",))

        self.assertEqual(db.infosetValue(graph_id, (graph_type,), None), ("Friendship",) )
        self.assertEqual(db.infosetValue(graph_id, (name,), v1), ("Alice",) )
        self.assertEqual(db.infosetValue(graph_id, (name,), v2), ("Bob",) )
        self.assertEqual(db.infosetValue(graph_id, (relationship,), e1), ("knows",) )
    # <<fold
    def testVertexDeletionCascade(self): # fold>>
        db = Database.Database()
        db.connect("db_testCreateInfoset")

        graph_id = db.createGraph()
        
        coords = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#Coords", 1))
        labels = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#AtomLabel", 1))
        bondtypes = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#BondType",2))
        angles = db.createInfoset(graph_id, InfosetType.InfosetType("http://example.com/#Angle",3))

        v1 = db.createVertex(graph_id)
        v2 = db.createVertex(graph_id)
        v3 = db.createVertex(graph_id)
        link = db.createNEdge(graph_id, (v1,v2))
        angle = db.createNEdge(graph_id, (v1,v2,v3))

        db.setInfosetValue(graph_id, (coords,), v1,( (10.0,0.0,0.0),) )
        db.setInfosetValue(graph_id, (coords,), v2,( (10.0,2.0,0.0),) )
        db.setInfosetValue(graph_id, (coords,), v3,( (10.0,2.0,3.0),) )

        db.setInfosetValue(graph_id, (bondtypes,), link, (2,))
        db.setInfosetValue(graph_id, (angles,), angle, (45.0,))

        db.deleteVertex(graph_id, v1)

        self.assertEqual(db.vertexCount(graph_id),2)
        self.assertEqual(db.nEdgeCount(graph_id, dimensionality=2),0)
        self.assertEqual(db.nEdgeCount(graph_id, dimensionality=3),0)

        # <<fold
        

if __name__ == '__main__':
    unittest.main()
    


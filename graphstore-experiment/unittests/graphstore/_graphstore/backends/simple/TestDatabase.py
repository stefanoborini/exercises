# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../../../"));
import unittest
import time


from graphstore._graphstore.backends.simple import Database

def moduleDir():
    return os.path.dirname(__file__)

class TestDatabase(unittest.TestCase):
    def testiInitX(self):
        g = Database.Database()

        self.assertEqual(g.__class__, Database.Database)

    def testConnect(self):
        g = Database.Database()
        g.connect("db_testConnect")
        
        self.assertEqual(0,0)

    def testCreateGraph(self):
        g = Database.Database()
        g.connect("db_testCreateGraph")
        
        id = g.createGraph()

        self.assertNotEqual(id, None)
       
    def testAllGraphs(self):
        g = Database.Database()
        g.connect("db_testAllGraphs")
        
        id1 = g.createGraph()
        id2 = g.createGraph()

        self.assertEqual(len(g.allGraphs()),2)
        self.assertTrue(id1 in g.allGraphs())
        self.assertTrue(id2 in g.allGraphs())
        
    def testDbMetainfo(self):
        g = Database.Database()
        g.connect("db_testDbMetainfo")

        g.setDbMetainfo("test","123")
        self.assertEqual(g.dbMetainfo("test"), "123")
        self.assertEqual(g.dbMetainfo("nothing"), None)
         


if __name__ == '__main__':
    unittest.main()
    


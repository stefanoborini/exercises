import _graphstore.Formatter

from _graphstore.Formatter import *

from _graphstore.backends.memory.Database import *

db=Database()
g=db.createGraph(name="grafo1")
g=db.createGraph()
g=db.createGraph()
g=db.createGraph(namespace="foo")
g=db.createGraph(namespace="xx")
f=Formatter(db)
f.printGraphList()

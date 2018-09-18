import graphstore

db = graphstore.newDatabase(backend="memory")

db.connect("/foo")
db.init()
g = db.createGraph()
db.createVertex(g)

db = graphstore.newDatabase(backend="mysql")
db.init()
g = db.createGraph()
db.createVertex(g)

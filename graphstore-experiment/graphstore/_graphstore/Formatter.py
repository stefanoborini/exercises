
class Formatter(object):
    def __init__(self, db):
        self._db = db

    def printGraphList(self):
        for g_id in self._db.allGraphs():
            print str(self._db.getGraphNamespace(g_id))+'/'+str(self._db.getGraphName(g_id))


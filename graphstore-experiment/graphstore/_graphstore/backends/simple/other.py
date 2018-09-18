class Graph:
    def __init__(self): # fold>>
        self._entities = { 0: [ self ], 1 : [] }
        self._infosets = { 0: [], 1: []}
        self._oid = 1
        self._uuid = uuid.uuid4()
        # <<fold 
    def entityList(self, dimensionality): # fold>>
        if self._entities.has_key(dimensionality):
            return self._entities[dimensionality]
        return []
        # <<fold
    def createEntity(self, entities=None): # fold>>
        if entities is None:
            id = self._oid
            self._entities[1].append(id)
            for infoset in self._infosets[1]:
                infoset._addSpace(id)
            self._oid += 1
            return id
        
        dimensionality = len(entities)
        if not self._entities.has_key(dimensionality):
            self._entities[dimensionality] = []

        self._entities[dimensionality].append(entities)

        # sync infosets
        if not self._infosets.has_key(dimensionality):
            self._infosets[dimensionality] = []

        for infoset in self._infosets[dimensionality]:
            infoset._addSpace(entities)

        return entities
        # <<fold
    def deleteEntity(self, entity): # fold>>
        if type(entity) == types.TupleType:
            dimensionality = len(entity)
            self._entities[dimensionality].remove(entity)
            for infoset in self._infosets[dimensionality]:
                infoset._removeSpace(entity)
        else:
            self._entities[1].remove(entity)
            for infoset in self._infosets[1]:
                infoset._removeSpace(entity)

            for k,l in self._entities.items():
                if k == 0 or k == 1: continue
                for e in l:
                    if entity in e:
                        l.remove(e)
                        if self._infosets.has_key(len(e)):
                            for infoset in self._infosets[len(e)]:
                                try:
                                    infoset._removeSpace(e)
                                except:
                                    pass
        # <<fold
    def getInfosets(self, dimensionality=None, infoset_type=None, uuid=None): # fold>>
        infosets = None
        if dimensionality is not None:
            if not self._infosets.has_key(dimensionality):
                return []
            infosets = self._infosets[dimensionality]
        else:
            infosets = list( itertools.chain(*self._infosets.values())) # all of them

        if infoset_type is not None:
            infosets = filter(lambda x: x.type() == infoset_type, infosets)

        if uuid is not None:
            infosets = filter(lambda x: x.uuid() == uuid, infosets)

        return infosets
        # <<fold
    def uuid(self): # fold>>
        return self._uuid 
    # <<fold
    def _registerInfoset(self, infoset): # fold>>
        dimensionality = infoset.dimensionality()
        if not self._infosets.has_key(dimensionality):
            self._infosets[dimensionality] = []
        self._infosets[dimensionality].append(infoset)

        if not self._entities.has_key(dimensionality):
            self._entities[dimensionality] = []
        for entity in self._entities[dimensionality]:
            infoset._addSpace(entity)
        # <<fold


import uuid
import types

class Infoset(object):
    def __init__(self, graph, infoset_type): # fold>>
        self._graph = graph
        self._infoset_type = infoset_type
        self._uuid = uuid.uuid4()
        self._data = {}
        self._reifications = {}
        self._graph._registerInfoset(self)

    # <<fold
    def graph(self): # fold>>
        return self._graph
    # <<fold
    def uuid(self): # fold>>
        return self._uuid
    # <<fold
    def typeURI(self): # fold>>
        return self._infoset_type.typeURI()
    # <<fold
    def dimensionality(self): # fold>>
        return self._infoset_type.dimensionality()
    # <<fold
    def type(self): # fold>>
        return self._infoset_type
    # <<fold
    def size(self): # fold>>
        return len(self._data)
    # <<fold
    def hasNone(self): # fold>>
        return None in self._data.values()
    # <<fold
    def value(self, entity): # fold>>
        if type(entity) == types.TupleType:
            if len(entity) != self._infoset_type.dimensionality():
                raise ValueException("Invalid length for entity")
            return self._data[entity]
        elif self._infoset_type.dimensionality() == 0:
            return self._data[self._graph]
        else:
            return self._data[entity]
    # <<fold
    def setValue(self, entity, value): # fold>>
            
        if type(entity) == types.TupleType:
            if len(entity) != self._infoset_type.dimensionality():
                raise ValueException("Invalid length for entity")
            self._data[tuple(entity)] = value
        elif self._infoset_type.dimensionality() == 0:
            self._data[self._graph] = value
        else:
            self._data[entity] = value
    # <<fold

    def _addSpace(self, entity): # fold>>
        self._data[entity]=None
    # <<fold
    def _removeSpace(self, entity): # fold>>
        del self._data[entity]
    # <<fold

    def allValues(self): # fold>>
        return self._data.items()
    # <<fold
    def reify(self, type_uri, value): # fold>>
        reification_uuid = uuid.uuid4()
        self._reifications[reification_uuid] = (type_uri, value)
        return reification_uuid
    # <<fold 
    def getReifications(self, id=None): # fold>>
        if id is not None:
            if self._reifications.has_key(id):
                return self._reifications[id]
            return None
        else:
            return self._reifications.values()
    # <<fold



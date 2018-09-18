class InfosetType: 
    def __init__(self, type_uri, dimensionality): # fold>>
        self._type_uri = type_uri
        self._dimensionality = dimensionality
    # <<fold
    def typeURI(self): # fold>>
        return self._type_uri
    # <<fold
    def dimensionality(self): # fold>>
        return self._dimensionality
    # <<fold
    def __cmp__(self, other): # fold>>
        if isinstance(other, InfosetType):
            if cmp(self.dimensionality(), other.dimensionality()) != 0:
                return cmp(self.dimensionality(), other.dimensionality())
            if cmp(self.typeURI(), other.typeURI()) != 0:
                return cmp(self.typeURI(), other.typeURI()) 
            return 0
        return NotImplemented
    # <<fold
    def __hash__(self): # fold>>
        return hash(self.dimensionality()) ^ hash(self.typeURI())
    # <<fold



import backends.memory.Database

def newDatabase(backend):
    if backend == "memory":
        return backends.memory.Database.Database()
    else:
        raise Exception("Unrecognized backend "+backend)







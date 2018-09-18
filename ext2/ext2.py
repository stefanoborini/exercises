import struct 

class SuperBlock:
    def __init__(self, file):
        self.file = file
        self.file.seek(1024)
        print struct.unpack("IIIIIIIIIIIIIHHHHHHIIIIHHIHHIII16s16s64sI",self.file.read(204))


f=file("pippo","rb")
s=SuperBlock(f)

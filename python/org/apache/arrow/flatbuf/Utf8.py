# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# Unicode with UTF-8 encoding
class Utf8(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUtf8(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Utf8()
        x.Init(buf, n + offset)
        return x

    # Utf8
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def Utf8Start(builder): builder.StartObject(0)
def Utf8End(builder): return builder.EndObject()

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# Same as Utf8, but with 64-bit offsets, allowing to represent
# extremely large data values.
class LargeUtf8(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLargeUtf8(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LargeUtf8()
        x.Init(buf, n + offset)
        return x

    # LargeUtf8
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def LargeUtf8Start(builder): builder.StartObject(0)
def LargeUtf8End(builder): return builder.EndObject()

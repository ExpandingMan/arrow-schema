# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

class FixedSizeBinary(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFixedSizeBinary(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedSizeBinary()
        x.Init(buf, n + offset)
        return x

    # FixedSizeBinary
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Number of bytes per value
    # FixedSizeBinary
    def ByteWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def FixedSizeBinaryStart(builder): builder.StartObject(1)
def FixedSizeBinaryAddByteWidth(builder, byteWidth): builder.PrependInt32Slot(0, byteWidth, 0)
def FixedSizeBinaryEnd(builder): return builder.EndObject()
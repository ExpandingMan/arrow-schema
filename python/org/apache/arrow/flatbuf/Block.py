# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Block(object):
    __slots__ = ['_tab']

    # Block
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Index to the start of the RecordBlock (note this is past the Message header)
    # Block
    def Offset(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Length of the metadata
    # Block
    def MetaDataLength(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # Length of the data (this is aligned so there can be a gap between this and
    # the metadata).
    # Block
    def BodyLength(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))

def CreateBlock(builder, offset, metaDataLength, bodyLength):
    builder.Prep(8, 24)
    builder.PrependInt64(bodyLength)
    builder.Pad(4)
    builder.PrependInt32(metaDataLength)
    builder.PrependInt64(offset)
    return builder.Offset()

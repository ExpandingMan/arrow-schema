# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Time type. The physical storage type depends on the unit
# - SECOND and MILLISECOND: 32 bits
# - MICROSECOND and NANOSECOND: 64 bits
class Time(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTime(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Time()
        x.Init(buf, n + offset)
        return x

    # Time
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Time
    def Unit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 1

    # Time
    def BitWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 32

def TimeStart(builder): builder.StartObject(2)
def TimeAddUnit(builder, unit): builder.PrependInt16Slot(0, unit, 1)
def TimeAddBitWidth(builder, bitWidth): builder.PrependInt32Slot(1, bitWidth, 32)
def TimeEnd(builder): return builder.EndObject()

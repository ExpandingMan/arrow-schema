# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# ----------------------------------------------------------------------
# Arrow File metadata
#
class Footer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFooter(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Footer()
        x.Init(buf, n + offset)
        return x

    # Footer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Footer
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Footer
    def Schema(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Schema import Schema
            obj = Schema()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Footer
    def Dictionaries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 24
            from .Block import Block
            obj = Block()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Footer
    def DictionariesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Footer
    def RecordBatches(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 24
            from .Block import Block
            obj = Block()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Footer
    def RecordBatchesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # User-defined metadata
    # Footer
    def CustomMetadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .KeyValue import KeyValue
            obj = KeyValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Footer
    def CustomMetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def FooterStart(builder): builder.StartObject(5)
def FooterAddVersion(builder, version): builder.PrependInt16Slot(0, version, 0)
def FooterAddSchema(builder, schema): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(schema), 0)
def FooterAddDictionaries(builder, dictionaries): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(dictionaries), 0)
def FooterStartDictionariesVector(builder, numElems): return builder.StartVector(24, numElems, 8)
def FooterAddRecordBatches(builder, recordBatches): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(recordBatches), 0)
def FooterStartRecordBatchesVector(builder, numElems): return builder.StartVector(24, numElems, 8)
def FooterAddCustomMetadata(builder, customMetadata): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(customMetadata), 0)
def FooterStartCustomMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FooterEnd(builder): return builder.EndObject()
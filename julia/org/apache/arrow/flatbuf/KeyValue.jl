# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct KeyValue
#=
#  ----------------------------------------------------------------------
#  user defined key value pairs to add custom metadata to arrow
#  key namespacing is the responsibility of the user
=#
    key::String = ""
    value::String = ""
end
FlatBuffers.@ALIGN(KeyValue, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:KeyValue} = [
    0x00000004, 0x00000006
]

KeyValue(buf::AbstractVector{UInt8}) = FlatBuffers.read(KeyValue, buf)
KeyValue(io::IO) = FlatBuffers.deserialize(io, KeyValue)

end)

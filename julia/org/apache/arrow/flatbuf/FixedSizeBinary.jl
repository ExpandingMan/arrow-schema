# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct FixedSizeBinary
#=
#  Number of bytes per value
=#
    byteWidth::Int32 = 0
end
FlatBuffers.@ALIGN(FixedSizeBinary, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:FixedSizeBinary} = [
    0x00000004
]

FixedSizeBinary(buf::AbstractVector{UInt8}) = FlatBuffers.read(FixedSizeBinary, buf)
FixedSizeBinary(io::IO) = FlatBuffers.deserialize(io, FixedSizeBinary)

end)


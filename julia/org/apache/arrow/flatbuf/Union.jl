# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct Union
#=
#  A union is a complex type with children in Field
#  By default ids in the type vector refer to the offsets in the children
#  optionally typeIds provides an indirection between the child offset and the type id
#  for each child typeIds[offset] is the id used in the type vector
=#
    mode::UnionMode = 0
    typeIds::Vector{Int32} = []
end
FlatBuffers.@ALIGN(Union, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:Union} = [
    0x00000004, 0x00000006
]

Union(buf::AbstractVector{UInt8}) = FlatBuffers.read(Union, buf)
Union(io::IO) = FlatBuffers.deserialize(io, Union)

end)


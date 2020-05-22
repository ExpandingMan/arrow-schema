# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct TensorDim
#=
#  ----------------------------------------------------------------------
#  Data structures for dense tensors
#  Shape data for a single axis in a tensor
=#
#=
#  Length of dimension
=#
    size::Int64 = 0
#=
#  Name of the dimension, optional
=#
    name::String = ""
end
FlatBuffers.@ALIGN(TensorDim, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:TensorDim} = [
    0x00000004, 0x00000006
]

TensorDim(buf::AbstractVector{UInt8}) = FlatBuffers.read(TensorDim, buf)
TensorDim(io::IO) = FlatBuffers.deserialize(io, TensorDim)

end)

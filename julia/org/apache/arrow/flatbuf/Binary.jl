# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


mutable struct Binary
#=
#  Opaque binary data
=#
end
FlatBuffers.@ALIGN(Binary, 1)

Binary(buf::AbstractVector{UInt8}) = FlatBuffers.read(Binary, buf)
Binary(io::IO) = FlatBuffers.deserialize(io, Binary)

end)


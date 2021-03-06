# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@STRUCT struct Block
#=
#  Index to the start of the RecordBlock (note this is past the Message header)
=#
    offset::Int64
#=
#  Length of the metadata
=#
    metaDataLength::Int32
#=
#  Length of the data (this is aligned so there can be a gap between this and
#  the metadata).
=#
    bodyLength::Int64
end
FlatBuffers.@ALIGN(Block, 8)

Block(buf::AbstractVector{UInt8}) = FlatBuffers.read(Block, buf)
Block(io::IO) = FlatBuffers.deserialize(io, Block)

end)


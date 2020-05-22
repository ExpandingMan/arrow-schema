# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote

#=
#  Provided for forward compatibility in case we need to support different
#  strategies for compressing the IPC message body (like whole-body
#  compression rather than buffer-level) in the future
=#
@enum BodyCompressionMethod::Int8 begin
#=
#  Each constituent buffer is first compressed with the indicated
#  compressor, and then written with the uncompressed length in the first 8
#  bytes as a 64-bit little-endian signed integer followed by the compressed
#  buffer bytes (and then padding as required by the protocol). The
#  uncompressed length may be set to -1 to indicate that the data that
#  follows is not compressed, which can be useful for cases where
#  compression does not yield appreciable savings.
=#
    BodyCompressionMethodBUFFER = 0
end


end)


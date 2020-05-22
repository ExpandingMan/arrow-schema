# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct Time
#=
#  Time type. The physical storage type depends on the unit
#  - SECOND and MILLISECOND: 32 bits
#  - MICROSECOND and NANOSECOND: 64 bits
=#
    unit::TimeUnit = 1
    bitWidth::Int32 = 32
end
FlatBuffers.@ALIGN(Time, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:Time} = [
    0x00000004, 0x00000006
]

Time(buf::AbstractVector{UInt8}) = FlatBuffers.read(Time, buf)
Time(io::IO) = FlatBuffers.deserialize(io, Time)

end)

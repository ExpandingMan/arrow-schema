# automatically generated by the FlatBuffers compiler, do not modify

org.apache.arrow.flatbuf.eval(quote


FlatBuffers.@with_kw mutable struct Timestamp
#=
#  Time elapsed from the Unix epoch, 00:00:00.000 on 1 January 1970, excluding
#  leap seconds, as a 64-bit integer. Note that UNIX time does not include
#  leap seconds.
# 
#  The Timestamp metadata supports both "time zone naive" and "time zone
#  aware" timestamps. Read about the timezone attribute for more detail
=#
    unit::TimeUnit = 0
#=
#  The time zone is a string indicating the name of a time zone, one of:
# 
#  * As used in the Olson time zone database (the "tz database" or
#    "tzdata"), such as "America/New_York"
#  * An absolute time zone offset of the form +XX:XX or -XX:XX, such as +07:30
# 
#  Whether a timezone string is present indicates different semantics about
#  the data:
# 
#  * If the time zone is null or equal to an empty string, the data is "time
#    zone naive" and shall be displayed *as is* to the user, not localized
#    to the locale of the user. This data can be though of as UTC but
#    without having "UTC" as the time zone, it is not considered to be
#    localized to any time zone
# 
#  * If the time zone is set to a valid value, values can be displayed as
#    "localized" to that time zone, even though the underlying 64-bit
#    integers are identical to the same data stored in UTC. Converting
#    between time zones is a metadata-only operation and does not change the
#    underlying values
=#
    timezone::String = ""
end
FlatBuffers.@ALIGN(Timestamp, 1)
FlatBuffers.slot_offsets(::Type{T}) where {T<:Timestamp} = [
    0x00000004, 0x00000006
]

Timestamp(buf::AbstractVector{UInt8}) = FlatBuffers.read(Timestamp, buf)
Timestamp(io::IO) = FlatBuffers.deserialize(io, Timestamp)

end)


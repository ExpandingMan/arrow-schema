# automatically generated by the FlatBuffers compiler, do not modify

include("Schema_generated.jl")
if !isdefined(@__MODULE__(), :org) @__MODULE__().eval(:(module org __precompile__(false); import FlatBuffers end)) end
if !isdefined(org, :apache) org.eval(:(module apache __precompile__(false); import FlatBuffers end)) end
if !isdefined(org.apache, :arrow) org.apache.eval(:(module arrow __precompile__(false); import FlatBuffers end)) end
if !isdefined(org.apache.arrow, :flatbuf) org.apache.arrow.eval(:(module flatbuf __precompile__(false); import FlatBuffers end)) end
include("org/apache/arrow/flatbuf/SparseMatrixCompressedAxis.jl")
include("org/apache/arrow/flatbuf/SparseTensorIndexCOO.jl")
include("org/apache/arrow/flatbuf/SparseMatrixIndexCSX.jl")
include("org/apache/arrow/flatbuf/SparseTensorIndexCSF.jl")
include("org/apache/arrow/flatbuf/SparseTensorIndex.jl")
include("org/apache/arrow/flatbuf/SparseTensor.jl")

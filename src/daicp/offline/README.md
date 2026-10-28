# Offline: Data and Knowledge

This package prepares two independent artifact types for local analysis:

1. Observed incidents, with evaluation references stored separately.
2. A vector index of approved technical documents, with chunk-level provenance.

`data/` owns auditing and preparation; `indexing/` owns ingestion, chunking, and
index construction. Both reuse `daicp.contracts`. The backend consumes their
artifacts without importing offline processing code.

See [data preparation](data/README.md) and [knowledge indexing](indexing/README.md)
for inputs, outputs, and examples. Original sources and audit notebooks remain
unchanged. Importing this package does not approve documents or run transformations.

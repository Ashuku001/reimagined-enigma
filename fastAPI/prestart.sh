CREATE EXTENSION embedding;

CREATE EXTENSION vector;

CREATE INDEX ON vectors USING hnsw(vec) WITH (maxelements=10000, dims=1536, m=3, efconstruction=16, efsearch=16);
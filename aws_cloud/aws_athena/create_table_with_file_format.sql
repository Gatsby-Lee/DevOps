-- It's all EXTERNAL TABLE

-- default file format: TEXTFILE
CREATE TABLE my_db.default_default (
  clsuter_id string
)
LOCATION 's3://aws-athena/my_db/default_default'


CREATE TABLE my_db.parquet_default (
  clsuter_id string
)
STORED AS PARQUET
LOCATION 's3://aws-athena/my_db/parquet_default'


CREATE TABLE my_db.orc_default (
  clsuter_id string
)
STORED AS ORC
LOCATION 's3://aws-athena/my_db/orc_default'


-- default and supported compression
-- ref: https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html

-- ---------------------
-- Set ORC's compression
-- ---------------------
CREATE TABLE my_db.orc_snappy (
  clsuter_id string
)
STORED AS ORC
LOCATION 's3://aws-athena/my_db/orc_snappy'
TBLPROPERTIES ("orc.compress"="SNAPPY");

-- disable compression
CREATE TABLE my_db.orc_uncompressed (
  clsuter_id string
)
STORED AS ORC
LOCATION 's3://aws-athena/my_db/orc_uncompressed'
TBLPROPERTIES ("orc.compress"="NONE");


-- -------------------------
-- Set Parquet's compression
-- -------------------------
CREATE TABLE my_db.parquet_snappy (
  clsuter_id string
)
STORED AS PARQUET
LOCATION 's3://aws-athena/my_db/parquet_snappy'
TBLPROPERTIES ("parquet.compression"="SNAPPY");

-- disable compression
CREATE TABLE my_db.parquet_uncompressed (
  clsuter_id string
)
STORED AS PARQUET
LOCATION 's3://aws-athena/my_db/parquet_uncompressed'
TBLPROPERTIES ("parquet.compression"="UNCOMPRESSED");


-- -------------------------
-- Set TEXTFILE's compression
-- -------------------------
CREATE TABLE my_db.textfile_gzip (
  clsuter_id string
)
STORED AS TEXTFILE
LOCATION 's3://aws-athena/my_db/textfile_gzip'
TBLPROPERTIES ("parquet.compression"="GZIP");

-- disable compression
CREATE TABLE my_db.textfile_uncompressed (
  clsuter_id string
)
STORED AS TEXTFILE
LOCATION 's3://aws-athena/my_db/textfile_uncompressed'
TBLPROPERTIES ("write.compression"="NONE");

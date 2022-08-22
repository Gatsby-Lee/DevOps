-- Table schema with JSON output format
CREATE EXTERNAL TABLE `discover_cluster_tickets_dummy_json_v1`(
  `cluster_id` string,
  `created_date` timestamp
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE
LOCATION 's3://aws-athena/my_db/dummy_json_v1/';

-- INSERT stmt
INSERT INTO dummy_json_v1 (cluster_id, created_date) VALUES ('89f921dc', timestamp '2022-03-24 17:45:02.0');


-- CREATE JSON output format data with CTAS
CREATE TABLE my_db.dummy_json_v1 
WITH (
     format = 'JSON',  
     external_location = 's3://aws-athena/my_db/dummy_json_v1'
) 
AS SELECT *
FROM my_db.dummy_orc_v1;


-- expected content in file
{"cluster_id":"89f921dc","created_date":"2022-03-24 17:45:02.0"}
{"cluster_id":"a420cac4","created_date":"2022-07-21 21:13:28.0"}

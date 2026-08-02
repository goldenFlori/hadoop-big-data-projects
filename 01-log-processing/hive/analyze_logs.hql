-- NASA Log Analysis with Hive
-- This script analyzes HTTP status codes from NASA access logs

-- Create table for NASA logs with regex parsing
CREATE TABLE IF NOT EXISTS nasa_logs (
  host STRING,
  log_timestamp STRING,
  request STRING,
  status_code INT,
  bytes INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
  "input.regex" = "^(\\S+) \\S+ \\S+ \\[([^\\]]+)\\] \"([^\"]+)\" (\\d{3}) (\\d+|-).*$"
)
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/';

-- Query: Count HTTP status codes
SELECT status_code, COUNT(*) AS count
FROM nasa_logs
WHERE status_code IS NOT NULL
GROUP BY status_code
ORDER BY count DESC;

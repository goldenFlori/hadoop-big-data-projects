NASA Web Server Log Analysis
Analyzed 1.9M HTTP requests from NASA's 1995 server logs on a Hadoop cluster.

MapReduce (Python): implemented the raw map→shuffle→reduce pattern to understand the fundamentals.
Hive (SQL): performed the same analysis with SQL — faster to write and the production-standard approach.
Result: ~89% success (200), with 10.8K broken-link (404) hits identified.
Stack: Hadoop, HDFS, MapReduce, Hive, Docker.
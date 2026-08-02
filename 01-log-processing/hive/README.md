# Hive Analysis

Same log analysis as MapReduce but using SQL.

## Setup

```bash
hadoop fs -mkdir -p /user/hive/warehouse
hadoop fs -put ../mapreduce/data/access.log /user/hive/warehouse/

# first time only
schematool -dbType derby -initSchema
```

## Run

```bash
hive -f analyze_logs.hql
```

Or interactive:
```bash
hive
source analyze_logs.hql;
```

## Results

Status code distribution (same as MapReduce output):
- 200: 1,701,534
- 304: 132,627
- 302: 46,573
- 404: 10,832
- Others: <100 each

Took about 30 seconds for 205MB data.

## Notes

Using RegexSerDe to parse log lines automatically instead of writing custom mapper code. Less flexible but way cleaner for standard formats.

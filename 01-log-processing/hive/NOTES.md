# Work Notes

## Issues I ran into

1. Had to reformat namenode because cluster IDs didn't match - datanode wouldn't start
2. Hive metastore kept giving schema errors, had to rm -rf metastore_db and reinit
3. First query hung forever - forgot to start YARN (need both dfs and yarn running)
4. "timestamp" is reserved in Hive, renamed to log_timestamp

## Regex pattern

Spent time getting this right:
```
^(\\S+) \\S+ \\S+ \\[([^\\]]+)\\] \"([^\"]+)\" (\\d{3}) (\\d+|-).*$
```

Matches Apache common log format. The tricky part was the quoted request field because it has spaces inside.

## Performance

Query took ~30 sec for 205MB. Ran 2 MR jobs:
- Job 1: count by status code
- Job 2: sort results

Could probably optimize with Tez or Spark execution engine instead of MR but this works fine for now.

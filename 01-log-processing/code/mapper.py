#!/usr/bin/env python3
"""Mapper: read access-log lines, emit (status_code, 1)."""
import sys, re
# Common Log Format: host - - [time] "METHOD /path HTTP/x.x" status bytes
LOG_RE = re.compile(r'^(\S+) \S+ \S+ \[.*?\] "(.*?)" (\d{3}) (\S+)')
for line in sys.stdin:
    m = LOG_RE.match(line)
    if not m:
        continue                 # skip malformed lines
    print(f"{m.group(3)}\t1")     # group(3) = status code

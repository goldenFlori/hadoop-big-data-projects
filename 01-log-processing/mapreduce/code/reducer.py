#!/usr/bin/env python3
"""Reducer: sum counts per status code (input arrives sorted by key)."""
import sys
current, total = None, 0
for line in sys.stdin:
    key, value = line.rstrip("\n").split("\t")
    if key == current:
        total += int(value)
    else:
        if current is not None:
            print(f"{current}\t{total}")
        current, total = key, int(value)
if current is not None:
    print(f"{current}\t{total}")

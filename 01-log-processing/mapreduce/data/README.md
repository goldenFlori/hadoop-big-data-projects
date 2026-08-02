# Dataset

## Full Dataset (205MB)

Due to GitHub file size limits, the full dataset is not included in this repo.

**Download:** [NASA HTTP Logs (July 1995)](http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html)

Or use this direct link:
```bash
wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz
gunzip NASA_access_log_Jul95.gz
mv NASA_access_log_Jul95 access.log
```

## Sample Data

`access_sample.log` contains 10,000 lines for testing the scripts locally.

## Dataset Info

- **Source:** NASA Kennedy Space Center web server
- **Period:** July 1995
- **Size:** 205MB (1.9M requests)
- **Format:** Apache Common Log Format

Example line:
```
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
```

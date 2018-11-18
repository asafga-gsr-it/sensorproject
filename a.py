session = gps(**opts)
session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)
for report in session:
    print report

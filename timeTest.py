import datetime, time
targetTime = datetime.datetime(2019, 9, 9, 21, 4, 0)
while datetime.datetime.now() < targetTime:
    time.sleep(1)

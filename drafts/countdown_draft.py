import datetime
import time


def countdown_draft(t=5):
    start = {"Intrare in parcare": str(datetime.datetime.now())}

    while t:
        time.sleep(1)
        t -= 1

    end = {"Parcarea a expirat": str(datetime.datetime.now())}

    timp = start | end

    return timp

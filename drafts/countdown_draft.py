import datetime
import time


def countdown(t):
    start = str(datetime.datetime.now())
    intrare = {"Intrare in parcare": start}

    timp = intrare

    print(timp)

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print({"Timp": timer}, end="\r")  # Overwrite the line each second
        time.sleep(1)
        t -= 1

    end = str(datetime.datetime.now())
    expirare = {"Parcarea a expirat": end}

    timp = expirare

    print(timp)

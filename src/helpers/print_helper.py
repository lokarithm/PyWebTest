import time


def countDown(event_name, time_interval):
    while time_interval > 0:
        print(f"{event_name} starts in: {str(time_interval)}")
        time.sleep(1)
        time_interval -= 1

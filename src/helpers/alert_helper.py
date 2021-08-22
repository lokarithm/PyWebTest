import os
import platform
import time

try:
    # this module only works in Windows
    import winsound
except ImportError:
    print("Running in non windows sytem")


class AlertHelper:
    def __init__(self):
        self.currentOS = platform.system()

    def beep(self, duration):
        if self.currentOS == "Linux":
            self.__beep_linux(duration)
        if self.currentOS == "Windows":
            self.__beep_windows(duration)

    def __beep_linux(self, duration, frequency=440):
        os.system('play -nq -t alsa synth {} sine {}',
                  format(duration, frequency))

    def __beep_windows(self, duration, frequency=440):
        # convert duration from second to millisecond
        duration *= 1000
        while duration > 0:
            winsound.Beep(frequency, 1000)
            time.sleep(1)
            duration -= 1000

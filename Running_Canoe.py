# This is a sample Python script.

import time, os, sys

if "C:\\Users\\bensa\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\win32com\\client" in sys.path:
    pass
else:
    sys.path.append(
        "C:\\Users\\bensa\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\win32com\\client")

from win32com.client import *
from win32com.client.connect import *


def DoEvents():
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)


def DoEventsUntil(cond):
    while not cond():
        DoEvents()


class CanoeSync(object):
    """Wrapper class for CANoe Application object"""
    Started = False
    Stopped = False
    ConfigPath = ""

    def __init__(self):
        app = DispatchEx('CANoe.Application')
        app.Configuration.Modified = False
        ver = app.Version
        print('Load CANOE version ',
              ver.major, '-',
              ver.minor, '-',
              ver.Build, '...', sep='')
        self.App = app
        self.Measurement = app.Measurement
        self.Running = lambda : self.Measurement.Running
        self.WaitForStart = lambda: DoEventsUntil(lambda: CanoeSync.Started)
        self.WaitForStop = lambda: DoEventsUntil(lambda: CanoeSync.Stopped)
        WithEvents(self.App.Measurement, CanoeMeasurementEvents)

    def Start(self):
        if not self.Running():
            self.Measurement.Start()
            self.WaitForStart()

    def Stop(self):
        if self.Running():
            self.Measurement.Stop()
            self.WaitForStop()

class CanoeMeasurementEvents(object):
    """Handler for CANoe measurement events"""

    def OnStart(self):
        CanoeSync.Started = True
        CanoeSync.Stopped = False
        print(" < measurement started >")

    def OnStop(self):
        CanoeSync.Started = False
        CanoeSync.Stopped = True
        print(" < measurement stopped >")

# -------------------------------------------
# main
# -------------------------------------------
app = CanoeSync()
# start the measurement
app.Start()


print("starting : %s" % time.ctime())
time.sleep(5)
print("Ending: %s" % time.ctime())

# stops the measurement
app.Stop()
print("Stop Canoe")

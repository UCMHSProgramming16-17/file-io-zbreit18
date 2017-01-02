import time     # For sleep
from issTracker import getIssStatus, getIssTime, getIssPos

def mainProcess():
    while True:
        currentIssStatus     = getIssStatus()
        issPos               = getIssPos(currentIssStatus)
        timeOfMeasurement    = getIssTime(currentIssStatus)
        print(timeOfMeasurement)
        print( "Latitude: %s\nLongitude:%s\n" % (issPos['longitude'], issPos['latitude']) )

        time.sleep(5)

mainProcess()

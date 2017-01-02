import requests
import time

def getIssStatus():
    """Returns a dictionary that contains the current status of the ISS"""
    issURL = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(issURL)
    return r.json()


def getIssPos(issRequest):
    """Returns a dictionary containing the current lat and long of the ISS given a JSON dictionary"""
    return issRequest['iss_position']


def getIssTime(issRequest):
    """Returns the UNIX timestamp of the last ISS measurement"""
    rawTime = issRequest['timestamp']
    formattedTime = time.strftime('%A, %d %b %Y %H:%M:%S', time.localtime(rawTime))
    return formattedTime

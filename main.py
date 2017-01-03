# Import Statements
import matplotlib                        # The base library
matplotlib.use('TKAgg')                  # For support on Mac OS X
from mpl_toolkits.basemap import Basemap # For mapping capabilities
import matplotlib.pyplot as plt          # For showing the map and images
import matplotlib.animation as animation # For contiuous map updates
from issTracker import *                 # For tracking the ISS's position
import csv                               # For storing the data

# Generate the map
worldMap = Basemap()

# Skin the map with an image
worldMap.arcgisimage(service = 'ESRI_Imagery_World_2D', xpixels = 1500)

# List of all previous lons, lats, and times
lons  = []
lats  = []
times = []

# Create a CSV file to store the data
posDataFile = open('iss-location-data.csv', 'w')
csvWriter   = csv.writer(posDataFile, delimiter = ',')
csvWriter.writerow(['Time', 'Latitude', 'Longitude'])

# hasRun tracks whether the recordPosData function is running for the first time
# Necessary because the i parameter is 0 two times, so you have to ignore the first function call
hasRun = False

def recordPosData(i, hasRun):
    """Write the ISS data to a csv file"""
    if hasRun:
        csvWriter.writerow([times[i], lons[i], lats[i]])
    else:
        hasRun = True

def getCurrentPos():
    """Update the lat, lon, and time arrays with the current ISS position"""
    # Get current ISS info
    issStatus   = getIssStatus()
    issPos      = getIssPos(issStatus)
    currentTime = getIssTime(issStatus)
    currentLon  = issPos['longitude']
    currentLat  = issPos['latitude']
    # Update the lat, lon, and time lists with the current info
    lons.append(currentLon)
    lats.append(currentLat)
    times.append(currentTime)

def updatePos(i):
    """Plot the location of the ISS"""
    getCurrentPos()
    recordPosData(i, hasRun)

    # Create points on the map from the array of lats and lons
    xCoordinates, yCoordinates = worldMap(lons, lats)
    # Plot those points on the map
    issPoint = worldMap.plot(xCoordinates, yCoordinates, 'ro', markersize = 5)[0]
    issPoint.set_data(xCoordinates, yCoordinates)

# Set updatePos as the animation function.
# Run the function every 30s.
myAnimation = animation.FuncAnimation(plt.gcf(), updatePos, interval = 30000)

# Show the Map
plt.title("Movements of the International Space Station")
plt.show()
# Close the CSV file
posDataFile.close()

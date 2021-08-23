import csv
from HashTable import HashTable
from Classes import *
from datetime import datetime


def convert_time(time):
    return datetime.strptime(datetime.today().strftime('%Y-%m-%d') + ' ' + time, '%Y-%m-%d %H:%M')


# Read Locations [ID, Name, Address, City, State, Zip]
with open('./Data/WGUPS Location List.csv') as csvfile:
    locationData = csv.reader(csvfile, delimiter=',')
    locationCount = 0
    locationHashTable = HashTable()
    for rowData in locationData:
        location = Location(int(rowData[0]), rowData[1], rowData[2], rowData[3], rowData[4], rowData[5])
        locationHashTable.insert(rowData[2], location)
        locationCount += 1

# Special package 0 to deliver to hub
packageHashTable = HashTable()
end_time = convert_time('23:59')  # End of day (EOD)
package0 = Package(0, '4001 South 700 East', 'Salt Lake City', 'UT', '84107', end_time, '0', '', Status.EN_ROUTE, 0)
packageHashTable.insert(0, package0)

# Read Packages [ID, Address, City, State, Zip, Delivery Deadline, Mass KILO, Special Notes]
with open('./Data/WGUPS Package File.csv') as csvfile:
    packageData = csv.reader(csvfile, delimiter=',')
    next(packageData)  # skip header

    packageCount = 0
    for rowData in packageData:
        packageCount += 1
        key = int(rowData[0])
        if rowData[5] != 'EOD':
            deadline = datetime.strptime(datetime.today().strftime('%Y-%m-%d') + ' ' + rowData[5], '%Y-%m-%d %H:%M %p')
        else:
            deadline = convert_time('23:59')
        package = Package(int(rowData[0]), rowData[1], rowData[2], rowData[3], rowData[4], deadline, rowData[6],
                          rowData[7], Status.AT_HUB, locationHashTable.get(rowData[1]).id)

        packageHashTable.insert(key, package)

# Read Distances
with open('./Data/WGUPS Distance Table.csv') as csvfile:
    distanceData = csv.reader(csvfile, delimiter=',')
    i = 0
    distance = [[0.0 for col in range(locationCount)] for row in range(locationCount)]
    for rowData in distanceData:
        for col in range(0, i + 1):
            distance[i][col] = distance[col][i] = float(rowData[col])  # Undirected graph
        i += 1


def get_package_hash_table():
    return packageHashTable


def get_location_hash_table():
    return locationHashTable


def get_distance_map():
    return distance


def get_package_count():
    return packageCount


def get_location_count():
    return locationCount

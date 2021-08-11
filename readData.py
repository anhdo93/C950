import csv
from HashTable import HashTable
from Classes import Package

# Read Packages [ID, Address, City, State, Zip, Delivery Deadline, Mass KILO, Special Notes]
with open('./Data/WGUPS Package File.csv') as csvfile:
    packageData = csv.reader(csvfile, delimiter=',')
    next(packageData)  # skip header
    packageHashTable = HashTable()
    for rowData in packageData:
        key = int(rowData[0])
        package = Package(int(rowData[0]), rowData[1], rowData[2], rowData[3], rowData[4], rowData[5], rowData[6], rowData[7], 'AT_HUB')

        packageHashTable.insert(key, package)

# Read Locations [ID, Name, Address, City, State, Zip]
with open('./Data/WGUPS Location List.csv') as csvfile:
    location = list(csv.reader(csvfile, delimiter=','))
    n = len(list(location))

# Read Distances
with open('./Data/WGUPS Distance Table.csv') as csvfile:
    distanceData = csv.reader(csvfile, delimiter=',')
    i = 0
    distance = [[0.0 for col in range(n)] for row in range(n)]
    for rowData in distanceData:
        for col in range(0, i + 1):
            distance[i][col] = distance[col][i] = float(rowData[col])  # Undirected graph
        i += 1


def get_package_hash_table():
    return packageHashTable


def get_distance_map():
    return distance


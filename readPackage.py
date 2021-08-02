import csv
from HashTable import HashTable

with open('./Data/WGUPS Package File.csv') as csvfile:
    packageData = csv.reader(csvfile, delimiter=',')
    next(packageData)  # skip header
    packageHashTable = HashTable()
    for row in packageData:
        # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        packageId = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deliveryDeadline = row[5]
        massKilo = row[6]
        specialNotes = row[7]
        deliveryStatus = 'At the hub'

        key = packageId
        value = [packageId, address, city, state, zip, deliveryDeadline, massKilo, specialNotes, deliveryStatus]

        packageHashTable.insert(key, value)


def get_package_hash_table():
    return packageHashTable



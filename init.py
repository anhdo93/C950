from readData import *

'''
    ASSUMPTIONS: results should be <140 miles for both trucks
    1. Two trucks
    2. 16 packages/truck
    3. Speed 18 mph
    4. Start @ 8:00am
    5. Package #9 - wrong address, to be updated to correct address of location #19
        (410 S State St., Salt Lake City, UT 84111) @ 10:20am
'''


# ASSUMPTIONS/INPUT/INITIALIZATION--------------------------------------------------------------------------------------
speed = 18  # Truck speed [18 mph]
truck = [1, 2, 3]  # Truck indices list
n = get_package_count()  # N - number of packages [40]
truck_package_limit = 16  # Each truck can hold up to [16 packages]

start_time = convert_time('8:00')
end_time = convert_time('23:59')  # End of day (EOD)
delayed_time = convert_time('9:05')  # Delayed package
update_time = convert_time('10:20')  # Address corrected

distance = get_distance_map()  # Import distance matrix
packageHashTable = get_package_hash_table()  # Import package hash table

package_list = [i for i in range(1, n+1)]  # Package list with package indices
packages_on_truck = [[0] for i in range(len(truck)+1)]  # Truck package list with required 'special' package 0 to hub
available = [truck_package_limit for i in range(len(truck)+1)]  # Space available on truck
route_for_truck = [[] for i in range(len(truck)+1)]  # Route with location id for corresponding truck



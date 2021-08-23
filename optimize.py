from readData import *
from datetime import timedelta

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
start_time = [convert_time('08:00') for i in range(len(truck)+1)]  # Delivery starts at 8:00 AM
end_time = convert_time('23:59')  # End of day (EOD)
delayed_time = convert_time('9:05')  # Delayed package
update_time = convert_time('10:20')  # Address corrected
start_time[2] = delayed_time  # Truck 2 starts at delayed time

distance = get_distance_map()  # Import distance matrix
packageHashTable = get_package_hash_table()  # Import package hash table

package_list = [i for i in range(1, n+1)]  # Package list with package indices
packages_on_truck = [[0] for i in range(len(truck)+1)]  # Truck package list with required 'special' package 0 to hub
available = [truck_package_limit for i in range(len(truck)+1)]  # Space available on truck
route_for_truck = [[] for i in range(len(truck)+1)]  # Route with location id for corresponding truck
mileage = [0 for i in range(len(truck)+1)]
total_mileage = 0


# FUNCTIONS-------------------------------------------------------------------------------------------------------------
def get_package(pkg_id):  # Get Package object from its hash table
    return packageHashTable.get(pkg_id)


def assigned_truck(pkg_id):  # Assign truck priority based on notes and deadline
    priority_truck = 3
    if get_package(pkg_id).deadline != end_time:  # Packages with specific deadline
        priority_truck = 1
    if pkg_id in [13, 14, 15, 16, 19, 20]:  # Packages with 'Must be delivered with ' notes
        priority_truck = 1
    if 'Can only be on truck 2' in get_package(pkg_id).notes:  # Packages required on truck 2
        priority_truck = 2
    if 'Delayed on flight' in get_package(pkg_id).notes:  # Delayed packages
        priority_truck = 2
    if 'Wrong address listed' in get_package(pkg_id).notes:  # Packages with wrong address
        priority_truck = 3
    return priority_truck


def load(pkg_id, t):
    packages_on_truck[t].append(pkg_id)
    available[t] -= 1
    if get_package(pkg_id).location_id not in route_for_truck[t]:
        route_for_truck[t].append(get_package(pkg_id).location_id)


def diff_distance(v1, v2, v3, v4):  # Distance difference between 4 vertices for 2-opt algorithm validation
    return (distance[v1][v3] + distance[v2][v4]) - (distance[v1][v2] + distance[v3][v4])


def optimized_route(route):  # 2-opt algorithm for avoiding crossing and optimize distance
    opt_route = route
    optimized = True
    while optimized:
        optimized = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                if diff_distance(opt_route[i - 1], opt_route[i], opt_route[j - 1], opt_route[j]) < 0:
                    opt_route[i:j] = opt_route[j - 1:i - 1:-1]
                    optimized = True
        route = opt_route
    return opt_route


# GREEDY ALGORITHM------------------------------------------------------------------------------------------------------
'''
    PSEUDOCODE 

    PACKAGES LOADING   
    Load Truck 1 (Time-sensitive) with time-sensitive packages
    Load Truck 2 (Required) with required and delayed packages
    Load Truck 3 with remaining EOD packages
        If (package is on the route of truck 1 or 2) and (space is available):
            Load package into corresponding truck
        Else:
            If truck 3 has available space:
                Load package into truck 3
            Else:
                Load into truck 2        

    PACKAGES DELIVERY                        
    Truck 1 delivery starts at 8:00 AM
    Truck 2 delivery starts at 9:05 AM
    Truck 3 delivery starts when truck 1 or 2 arrives at hub
    For package(s) with wrong address:
        Wait until 10:20am to update correct address            
'''
# Load packages into truck 1 and 2 based on priority
for pkg in package_list:
    t = assigned_truck(pkg)
    if (available[t] > 0) and (t == 1):
        load(pkg, t)
    if (available[t] > 0) and (t == 2):
        load(pkg, t)
# Load remaining packages into truck 1 and 2 if on the same route. If not, load into truck 3.
for pkg in package_list:
    t = assigned_truck(pkg)
    if t == 3:
        if get_package(pkg).location_id in route_for_truck[1]:  # Packages go to same destination for truck 1
            if available[1] > 0:
                load(pkg, 1)  # Load into truck 1
                continue
        if get_package(pkg).location_id in route_for_truck[2]:  # Packages go to same destination for truck 2
            if available[2] > 0:
                load(pkg, 2)  # Load into truck 2
                continue
        if available[t] > 0:  # Regular EOD packages should be loaded into truck 3
            load(pkg, t)
        else:  # If space not allowed, load into truck 2
            load(pkg, t-1)
# Calculate route with shortest distance to the next destination
for t in truck:
    route = [0]  # Initialized route starting at hub. Current location = route[-1]
    for i in route_for_truck[t]:
        min_dist = 50
        for j in route_for_truck[t]:
            if (distance[route[-1]][j] < min_dist) and (j not in route):  # Find closest destination to current location
                closest = j
                min_dist = distance[route[-1]][j]
        route.append(closest)
    route.remove(0)  # Remove starting point at hub
    route.append(0)  # Add ending point at hub
    route_for_truck[t] = route


# PACKAGES DELIVERY-----------------------------------------------------------------------------------------------------
for t in truck:
    if t == 3:
        start_time[t] = min(start_time[1], start_time[2])  # Truck 3 starts when either truck 1 or 2 arrives at hub

    current_location = 0
    package_index = 0

    route_for_truck[t] = optimized_route(route_for_truck[t])  # Optimize route with 2-opt algorithm
    print('--------- TRUCK {} ----------'.format(t))
    print('Truck {} Route: '.format(t), end='')
    print(*route_for_truck[t], sep=' --> ')
    print('Truck {} Packages: {}'.format(t, packages_on_truck[t]))

    for destination in route_for_truck[t]:
        for package in packages_on_truck[t]:
            # Find package with wrong address to update
            found_error = False
            current_package = get_package(package)
            if (current_package.location_id == destination) and ('Wrong address' in get_package(package).notes):
                error_package = current_package
                if error_package.status != Status.DELIVERED:
                    found_error = True
                    if start_time[t] < update_time:  # wait until update time to correct address
                        start_time[t] = update_time
                    error_package.address = '410 S State St'
                    error_package.city = 'Salt Lake City'
                    error_package.state = 'UT'
                    error_package.zip = '84111'
                    error_package.notes = 'Fixed address'
                    error_package.location_id = locationHashTable.get(error_package.address).id
            # Deliver package to destination
            if (current_package.location_id == destination) or found_error:
                current_package.status = Status.EN_ROUTE
                next_location = get_package(package).location_id
                delivery_time = start_time[t] + timedelta(hours=distance[current_location][next_location]/speed)
                mileage[t] += distance[current_location][next_location]
                if delivery_time > current_package.deadline:  # Check if package can arrive on time
                    current_package.status = Status.LATE
                else:
                    current_package.status = Status.DELIVERED
                if current_package.id != 0:
                    package_index += 1
                else:
                    package_index = 0
                print('{}-{:2} Package {:3}: {:>3} -> {:>3} [{:>4} miles ] Start: {}  Delivered: {} {:>19}  (Deadline {:>6})'
                      .format(t, package_index, current_package.id, current_location, next_location, distance[current_location][next_location],
                              start_time[t].strftime('%H:%M'), delivery_time.strftime('%H:%M'),
                              current_package.status, current_package.deadline.strftime('%H:%M')))
                current_location = next_location
                start_time[t] = delivery_time

    print('Total Mileage for Truck {} - {}'.format(t, mileage[t]))
    total_mileage += mileage[t]

print('TOTAL MILEAGE FOR ALL TRUCKS: {} miles'.format(total_mileage))
from functions import *

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


# NEAREST NEIGHBOR & 2-OPT ALGORITHMS-----------------------------------------------------------------------------------
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

    route_for_truck[t] = optimized_route(route)  # Optimize route with 2-opt algorithm

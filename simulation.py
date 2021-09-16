from functions import *
from init import *
import optimize
from datetime import timedelta


mileage = [0 for i in range(len(truck)+1)]
current_time = [start_time for i in range(len(truck) + 1)]  # Delivery starts at 8:00 AM
departure_time = current_time
departure_time[2] = delayed_time  # Truck 2 starts at delayed time


# PACKAGES DELIVERY-----------------------------------------------------------------------------------------------------
def run(printRoute):
    """Run package delivery simulation

    Space Complexity O(N)
    Time Complexity O(N^2)
    :param printRoute: True to enable printing, False to disable printing
    :return package delivery simulation report if printing enabled
    """
    if not printRoute:
        blockPrint()
    global current_time, mileage, departure_time
    current_time = [convert_time('08:00') for i in range(len(truck) + 1)]  # Delivery starts at 8:00 AM
    departure_time = [convert_time('08:00') for i in range(len(truck) + 1)]
    current_time[2] = delayed_time  # Truck 2 starts at delayed time
    departure_time[2] = delayed_time  # Truck 2 starts at delayed time
    mileage = [0 for i in range(len(truck) + 1)]  # Reset mileage every time simulation runs
    total_mileage = 0
    for t in truck:
        if t == 3:
            current_time[t] = min(current_time[1], current_time[2])  # Truck 3 starts when either truck 1 or 2 arrives at hub

        current_location = 0
        package_index = 0

        print(' TRUCK {} '.format(t).center(91, '-'))
        print('Route: 0 -> ', end='')
        print(*route_for_truck[t], sep=' -> ')
        print('Packages: {}'.format(packages_on_truck[t]))
        print_truck_header()

        for destination in route_for_truck[t]:
            for pkg in packages_on_truck[t]:
                found_error = False
                # Find package with wrong address to update
                current_package = get_package(pkg)
                current_package.truck = t  # Current package on truck t
                current_package.departure = departure_time[t]
                next_location = current_package.location_id
                if (get_package(pkg).location_id == destination) and ('Wrong address' in get_package(pkg).notes):
                    error_package = current_package
                    if not found_error:
                        found_error = True
                        if current_time[t] < update_time:  # wait until update time to correct address
                            current_time[t] = update_time
                        error_package.address = '410 S State St'
                        error_package.city = 'Salt Lake City'
                        error_package.state = 'UT'
                        error_package.zip = '84111'
                        next_location = locationHashTable.get(error_package.address).id
                # Deliver package to destination
                if (current_package.location_id == destination) or found_error:
                    current_package.status = Status.EN_ROUTE
                    delivery_time = current_time[t] + timedelta(hours=distance[current_location][next_location] / speed)
                    mileage[t] += distance[current_location][next_location]
                    current_package.arrival = delivery_time
                    if delivery_time > current_package.deadline:  # Check if package can arrive on time
                        current_package.status = Status.LATE
                    else:
                        current_package.status = Status.DELIVERED
                    if current_package.id != 0:
                        package_index += 1
                    else:
                        package_index = 0

                    print('| {:^5} | {:^5} | {:^3} | {:>2} -> {:>2} | {:^5} | {:^7} | {:^7} | {:^24} | {:^8} |'
                          .format(t, package_index, current_package.id, current_location,
                                  next_location, distance[current_location][next_location],
                                  current_time[t].strftime('%H:%M'), delivery_time.strftime('%H:%M'),
                                  current_package.status, current_package.deadline.strftime('%H:%M')))
                    current_location = next_location
                    current_time[t] = delivery_time

        print('Truck {} traveled {:.1f} miles'.format(t, mileage[t]))
        total_mileage += mileage[t]

    print('TOTAL MILEAGE: {} miles'.format(total_mileage))
    enablePrint()


def truck_mileage():
    """Print total mileage traveled by all trucks

    Space Complexity O(1)
    Time Complexity O(1)
    :return: total mileage traveled by all trucks
    """
    total_miles = 0
    for t in truck:
        print('Truck {} traveled {:.1f} miles'.format(t, mileage[t]))
        total_miles += mileage[t]
    print('TOTAL MILEAGE: {} miles'.format(total_miles))


def package_status(pkg, status_time):
    """Print package(s) status

    Space Complexity O(N)
    Time Complexity O(N)
    :param pkg: package index, 0 for all packages
    :param status_time: time at the consideration
    :return: package status
    """
    print_package_header()
    if pkg == 0:
        for pkg in package_list:

            if status_time <= get_package(pkg).departure:
                get_package(pkg).status = Status.AT_HUB
            elif status_time <= get_package(pkg).arrival:
                get_package(pkg).status = Status.EN_ROUTE
            else:
                get_package(pkg).status = Status.DELIVERED

            print(get_package(pkg))
    else:
        if status_time <= get_package(pkg).departure:
            get_package(pkg).status = Status.AT_HUB
        elif status_time <= get_package(pkg).arrival:
            get_package(pkg).status = Status.EN_ROUTE
        else:
            get_package(pkg).status = Status.DELIVERED
        print(get_package(pkg))
